from rest_framework.permissions import BasePermission


class isAdminOrEncargadoOrSuperUser(BasePermission):
    def has_permission(self, request, view):
        myUser = request.user
        if myUser.groups.filter(name__in=['Administrador','Encargado']).exists() or myUser.is_superuser:
            return True
        return False