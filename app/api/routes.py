from flask import Blueprint, request, jsonify
from ..models import db, uIm_schema, uIm_schemas, UserImages


api = Blueprint('api', __name__, url_prefix = '/api')


@api.route('/myimg/new/<user_id>',methods=['POST'])
def add_url(user_id):
    url=request.json['url']
    prio=request.json['prio']
    user_id=user_id

    print(f'BIG TESTER {user_id}')

    ui=UserImages(url,user_id , prio )

    db.session.add(ui)
    db.session.commit()

    response=uIm_schema.dump(ui)
    return jsonify(response)


# Slightly excessive 'getbyid' to work around the fact that these both just enter a id to signify what it wants
# Same with the post methods
@api.route('/myimg/getbyuserid/<a_user>', methods=['GET'])
def get_urls(a_user):
    uis=UserImages.query.filter_by(user_id=a_user).order_by(UserImages.prio.asc()).all()
    response=uIm_schemas.dump(uis)
    return jsonify(response)

@api.route('/myimg/get1/<entry_id>',methods=["GET"])
def get_url(entry_id):
    ui=UserImages.query.get(entry_id)
    response=uIm_schema.dump(ui)
    return jsonify(response)


@api.route('/myimg/update/<entry_id>', methods= ['POST','PUT'])
def update_url(entry_id):
    ui=UserImages.query.get(entry_id)
    ui.url=request.json['url']
    ui.prio=request.json['prio']
    ui.user_id=request.json['user_id']

    db.session.commit()
    response=uIm_schema.dump(ui)
    return jsonify(response)


@api.route('/myimg/<entry_id>', methods=['DELETE'])
def delete_url(entry_id):
    ui=UserImages.query.get(entry_id)
    db.session.delete(ui)
    db.session.commit()
    response=uIm_schema.dump(ui)
    return jsonify(response)
