from models.item import ItemModel
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field can't be left blank!")
    parser.add_argument('store_id', type=int, required=True, help="every item needs a store id!")

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name=name)
        if item is not None:
            return item.json()
        else:
            return {"message": "The item does not exist"}, 404

    def post(self, name):

        if ItemModel.find_by_name(name=name):
            return {'message': f"An item with name [{name}] Already exist"}, 400
        else:
            data = Item.parser.parse_args()
            item = ItemModel(name=name, **data)  # OR (name,data['price'], data['store_id'])
            item.save_to_db()
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name=name)
        if item is not None:
            item.delete_from_db()
            return {"message": "Item  deleted"}, 200
        else:
            return {"message": "Item is unavailable"}, 400

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name=name)
        if item is None:
            item = ItemModel(name=name, **data)  # OR (name,data['price'], data['store_id'])
            return item.json()
        else:
            item = ItemModel(data['price'])
            return item.json()
            ##problem updating the price takes 1 positional arg


class ItemList(Resource):
    def get(self):
        return {'items': [x.json() for x in
                          ItemModel.query.all()]}  # >>ItemModel.query.all()>>.all() returns all the objects in the db
