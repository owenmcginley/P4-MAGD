print(db.listings.aggregate([
    {
      $group: {
        _id: "$adress.neighbourhood_cleansed",
        average_rating: { $avg: "$reviews_info.score_rating" },
        total_listings: { $sum: 1 }
      }
    },
    {
      $match: {
        "_id": { $ne: null }
      }
    },
    {
      $sort: { average_rating: -1 }
    }
  ]))