from pydantic import UUID4, field_validator

from care.emr.models.organziation import OrganizationUser
from care.emr.resources.base import EMRResource
from care.emr.resources.role.spec import RoleSpec
from care.emr.resources.user.spec import UserSpec
from care.security.models import RoleModel
from care.users.models import User


class OrganizationUserBaseSpec(EMRResource):
    __model__ = OrganizationUser
    __exclude__ = ["user", "role"]


class OrganizationUserWriteSpec(OrganizationUserBaseSpec):
    user: UUID4
    role: UUID4

    @field_validator("user")
    @classmethod
    def validate_user(cls, user):
        if User.objects.filter(external_id=user).exists():
            return user
        raise ValueError("User does not exist")

    @field_validator("role")
    @classmethod
    def validate_role(cls, role):
        if RoleModel.objects.filter(external_id=role).exists():
            return role
        raise ValueError("Role does not exist")

    def perform_extra_deserialization(self, is_update, obj):
        if not is_update:
            obj.user = User.objects.get(external_id=self.user)
            obj.role = RoleModel.objects.get(external_id=self.role)


class OrganizationUserReadSpec(OrganizationUserBaseSpec):
    user: dict
    role: dict

    @classmethod
    def perform_extra_serialization(cls, mapping, obj):
        mapping["user"] = UserSpec.serialize(obj.user).to_json()
        mapping["role"] = RoleSpec.serialize(obj.role).to_json()
        return mapping
