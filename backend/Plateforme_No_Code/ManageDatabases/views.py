from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializer import *
from .utils import *


class CreateDatabaseAPIView(APIView):
    @swagger_auto_schema(request_body=CreateDatabaseRequestSerializer)
    def post(self, request):
        try:
            # Récupérer le nom de la base de données depuis les données POST
            db_name = request.data.get('db_name')
            
            # Se connecter à MongoDB
            client = connect_to_mongo()
            
            # Créer la base de données
            db = create_dataBase(client, db_name)
            
            attributes_to_add = {
                "Password":"",
                "email":"",
                "Date_creation": date.today(),
                "Date_update" :date.today()
            }
            success, message = Create_collection(db_name,'User')
            success, message = insert_to_collection(db_name, 'User', attributes_to_add)
            # Se déconnecter de MongoDB
            deconnect_from_mongo(client)
            
            return Response({"success": True, "message": "Base de données créée avec succès."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"success": False, "message": f"Erreur : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(request_body=CreateDatabaseRequestSerializer)    
    def put(self, request):
        try:
            new_db_name= request.data.get('db_name')
            old_db_name = request.data.get("old_db_name")
            success, message = rename_database(old_db_name, new_db_name)
            if success:
                return Response({"success": True, "message": message}, status=status.HTTP_200_OK)
            else:
                return Response({"success": False, "message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"success": False, "message": f"Erreur : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        
class CollectionAPIView(APIView):
    @swagger_auto_schema(request_body=CreateCollectionSerializer)
    def post(self, request):
        try:
            db_name = request.data.get('db_name')
            collection_name = request.data.get('collection_name')
            success, message = Create_collection(db_name, collection_name) 
            if success:
                return Response({"success": True, "message": message}, status=status.HTTP_201_CREATED)
            else:
                return Response({"success": False, "message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"success": False, "message": f"Erreur : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(query_serializer=DocumentSerializer)
    def delete(self, request):
        try:
            db_name = request.query_params.get('db_name')
            collection_name = request.query_params.get('collection_name')
            success, message = delete_collection(db_name, collection_name) 
            if success:
                return Response({"success": True, "message": message}, status=status.HTTP_200_OK)
            else:
                return Response({"success": False, "message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"success": False, "message": f"Erreur : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)     
        
    @swagger_auto_schema(request_body=CreateCollectionSerializer)
    def put(self, request):
        try:
            db_name = request.data.get('db_name')
            new_collection_name = request.data.get('collection_name')
            old_collection_name = request.data.get('old_collection_name')
            success, message = rename_collection(db_name, old_collection_name, new_collection_name)
            if success:
                return Response({"success": True, "message": message}, status=status.HTTP_200_OK)
            else:
                return Response({"success": False, "message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"success": False, "message": f"Erreur : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

class DocumentsAPIView(APIView):
    @swagger_auto_schema(query_serializer=DocumentSerializer)
    def get(self, request):
        try:
            db_name = request.query_params.get('db_name')
            collection_name = request.query_params.get('collection_name')
            success, result = get_documents(db_name, collection_name)
            if success:
                return Response({"success": True, "result": result}, status=status.HTTP_200_OK)
            else:
                return Response({"success": False, "message": result}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"success": False, "message": f"Erreur : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(request_body=CreateCollectionSerializer)
    def post(self, request):
        try:
            # Récupérer les attributs à ajouter depuis les données POST
            attributes_to_add = request.data.get('attributes')
            db_name = request.data.get('db_name')
            collection_name = request.data.get('collection_name')
            # Ajouter les attributs à la collection existante
            success, message = insert_to_collection(db_name, collection_name, attributes_to_add)
            
            if success:
                return Response({"success": True, "message": message}, status=status.HTTP_201_CREATED)
            else:
                return Response({"success": False, "message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"success": False, "message": f"Erreur : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(request_body=CreateCollectionSerializer)
    def put(self, request):
        try: 
            update_data= request.data.get('attributes')
            db_name = request.data.get('db_name')
            collection_name = request.data.get('collection_name')
            id = request.data.get('id')
            success, message = update_document(db_name,collection_name,id,update_data)
            if success:
                return Response({"success": True, "message": message}, status=status.HTTP_200_OK)
            else:
                return Response({"success": True, "message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
                return Response({"success": False, "message": f"Erreur : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=DocumentSerializer)
    def delete(self, request):
        try:
            db_name = request.query_params.get('db_name')
            collection_name = request.query_params.get('collection_name')
            id = request.query_params.get('id')
            success, message = delete_document(id,db_name, collection_name) 
            if success:
                return Response({"success": True, "message": message}, status=status.HTTP_200_OK)
            else:
                return Response({"success": False, "message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"success": False, "message": f"Erreur : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)  

class AttributesAPIView(APIView):
    @swagger_auto_schema(query_serializer=AttributesSerializer)
    def delete(self, request):
        try:
            db_name = request.query_params.get('db_name')
            collection_name = request.query_params.get('collection_name')
            attribute = request.query_params.get('attribute')
            success, message = delete_attribut(db_name, collection_name,attribute) 
            if success:
                return Response({"success": True, "message": message}, status=status.HTTP_200_OK)
            else:
                return Response({"success": False, "message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"success": False, "message": f"Erreur : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)  
    @swagger_auto_schema(request_body=AttributesSerializer)
    def put(self, request):
        try: 
            old_attribute_name= request.data.get('old_attribute_name')
            db_name = request.data.get('db_name')
            collection_name = request.data.get('collection_name')
            new_attribute_name = request.data.get('attribute')
            success, message = rename_attribute_in_collection(db_name,collection_name,old_attribute_name,new_attribute_name)
            if success:
                return Response({"success": True, "message": message}, status=status.HTTP_200_OK)
            else:
                return Response({"success": True, "message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
                return Response({"success": False, "message": f"Erreur : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(request_body=AttributesSerializer)
    def post(self, request):
        try:
            attribute_to_add = request.data.get('attribute')
            db_name = request.data.get('db_name')
            collection_name = request.data.get('collection_name')
            success, message = add_empty_attribute_to_collection(db_name, collection_name, attribute_to_add)
            if success:
                return Response({"success": True, "message": message}, status=status.HTTP_201_CREATED)
            else:
                return Response({"success": False, "message": message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"success": False, "message": f"Erreur : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

class DocumentFilterAPIView(APIView):
    @swagger_auto_schema(query_serializer=DocumentSerializer)
    def get(self, request):
        try:
            id = request.query_params.get('id')
            db_name = request.query_params.get('db_name')
            collection_name = request.query_params.get('collection_name')
            success, result = get_document_by_id(db_name, collection_name,id)
            if success:
                return Response({"success": True, "result": result}, status=status.HTTP_200_OK)
            else:
                return Response({"success": False, "message": result}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"success": False, "message": f"Erreur : {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)