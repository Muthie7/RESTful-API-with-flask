from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name=name)
        if store is not None:
            return store.json()  # ensures it returns a json store object{
        else:
            return {"message": "The store does not exist"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name=name):
            return {"message": f"store [{name}] already exist"}, 400
        else:
            store = StoreModel(name=name)
            try:
                store.save_to_db()
            except:
                return {'message': "Error occurred while creating store"}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name=name)
        if store:
            store.delete_from_db()
            return {"message": "Store has been deleted"}
        else:
            return {"message": f"The store {name} doesn't exist"}, 400


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
        # list(map(lambda store:store.json(),StoreModel))
