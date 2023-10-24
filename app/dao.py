def load_catelogies():
    return [{
        "id": 1,
        "name": "Mobile"
    }, {
        "id": 2,
        "name": "Tablet"
    },
        {
            "id": 3,
            "name": "Laptop"
        }
    ]


def load_product(kw):
    product = [
        {
            "id": 1,
            "name": "Iphone 15 Pro Max",
            "price": 200000,
            "image": "https://www.techone.vn/wp-content/uploads/2023/09/iphone-15-pro-max_2__5.webp"
        },
        {
            "id": 2,
            "name": "Iphone 15 Pro Max",
            "price": 200000,
            "image": "https://www.techone.vn/wp-content/uploads/2023/09/iphone-15-pro-max_2__5.webp"
        },
        {
            "id": 3,
            "name": "Iphone 15 Pro Max",
            "price": 200000,
            "image": "https://www.techone.vn/wp-content/uploads/2023/09/iphone-15-pro-max_2__5.webp"
        },
        {
            "id": 4,
            "name": "Ipad Pro",
            "price": 200000,
            "image": "https://www.techone.vn/wp-content/uploads/2023/09/iphone-15-pro-max_2__5.webp"
        },
        {
            "id": 5,
            "name": "Iphone 15 Pro Max",
            "price": 200000,
            "image": "https://www.techone.vn/wp-content/uploads/2023/09/iphone-15-pro-max_2__5.webp"
        }
    ]
    if kw:
        product = [p for p in product if p["name"].find(kw) >= 0]

    return product
