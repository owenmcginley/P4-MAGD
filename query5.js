db.listings.aggregate([
    // Realizar el lookup para unir con la colección de reviews
    {
        $lookup: {
            from: "reviews",
            localField: "id",
            foreignField: "listing_id",
            as: "reviews"
        }
    },
    // Filtrar alojamientos con al menos 10 reseñas
    {
        $match: {
            $expr: { $gte: [{ $size: "$reviews" }, 10] },
            review_scores_rating: { $gte: 4.5 }
        }
    },
    // Proyectar los campos deseados
    {
        $project: {
            _id: 0,
            name: 1,
            description: 1,
            amenities: 1,
            number_of_reviews: { $size: "$reviews" }
        }
    },
    // Ordenar por número de reseñas en orden descendente
    {
        $sort: { number_of_reviews: -1 }
    }
]);