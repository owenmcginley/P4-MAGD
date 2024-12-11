print(db.reviews.aggregate([
  {
    $lookup: {
      from: "listings",
      localField: "listing_id",
      foreignField: "id",
      as: "listing_details"
    }
  },
  {
    $unwind: "$listing_details"
  },
  {
    $match: {
      $and: [
        {
          $or: [
            { comments: { $regex: /excelent/i } },
            { comments: { $regex: /fantastic/i } }
          ]
        },
        { "listing_details.price": { $lte: 100 } }
      ]
    }
  }
]))