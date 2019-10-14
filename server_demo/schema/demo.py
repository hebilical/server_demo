from marshmallow import Schema, fields, INCLUDE


class UserSchare(Schema):
    weibo_id = fields.Integer(load_from='weiBoId')
    user_name = fields.String(load_from='userName')
    at_user_list = fields.String(load_from='atUserList')
    target_users_name = fields.String( load_from='targetUsersName')

    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE

user_schare = UserSchare()
