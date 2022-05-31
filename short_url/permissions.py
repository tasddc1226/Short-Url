from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    """
    본인이 생성한 short url인지 확인하기 위한 Custom permission
    """

    message = "You can not delete another user"

    def has_object_permission(self, request, view, obj):
        if request.method == SAFE_METHODS:
            return True
        print(obj, request.user)
        return obj == request.user


class IsOwnerOrReadOnly(BasePermission):
    """
    사용자가 개체의 소유자인지 확인하는 Custom permission
    """

    message = "You must be the owner of this object."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
