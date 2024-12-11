db.listings.aggregate([
    // Convertir el precio a número (si está como string)
    {
        $addFields: {
            price_numeric: { $toDouble: "$price" }
        }
    },
    {
        $group: {
            _id: "$city",
            avg_price: { $avg: "$price_numeric" },
            max_price: { $max: "$price_numeric" }
        }
    },
    {
        $addFields: {
            avg_price_percentage: {
                $multiply: [
                    { $divide: ["$avg_price", "$max_price"] },
                    100
                ]
            }
        }
    },
    {
        $project: {
            _id: 0,
            city: "$_id",
            avg_price: 1,
            avg_price_percentage: 1,
        }
    },
    {
        $sort: { avg_price: -1 }
    }
]);