db.listings.aggregate([

    {
        $lookup: {
            from: "calendar",
            localField: "id",
            foreignField: "listing_id",
            as: "calendar"    
        }    
    },
    {
        $unwind: "$calendar"
    },
    {
        $match: {
            $and: [
                {"calendar.date": {$gte: "2024-11-20", $lte: "2024-11-25"}},
                {"calendar.available": "t"},
                {"city": "menorca"},
                {$or: [{ "room_type": "Entire home/apt"} , { "room_type": "Private room" }]}
            ]    
        }
    },
    {
        $project: {
            _id : 0,
            id: 1,
            name: 1,
            "host.neighbourhood": 1,
            room_type: 1,
            "calendar.date": 1,
            "calendar.available": 1,
            price: 1
        }
    }
]).sort({price:1},{listing_id:1},{date:1})