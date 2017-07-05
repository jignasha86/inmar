import csv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apis.models import Location, Department, Category, Subcategory, FlatData
from apis.serializers import LocationSerializer, DepartmentSerializer, CategorySerializer, SubcategorySerializer, FlatDataSerializer

@api_view(['GET', 'POST'])
def location_list(request):
    if request.method == 'GET':
        items = Location.objects.all()
        serializer = LocationSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def location_detail(request, pk):
    try:
        item = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response(status=400)

    if request.method == 'GET':
        serializer = LocationSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LocationSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET'])
def location_rel(request, pk):
    if request.method == 'GET':
        try:
            item = Location.objects.get(pk=pk)
        except Location.DoesNotExist:
               return Response(status=400)
        items = Department.objects.filter(location=item).all()
        serializer = DepartmentSerializer(items, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def department_list(request):
    if request.method == 'GET':
        items = Department.objects.all()
        serializer = DepartmentSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        location = Location.objects.get(id=request.data['location'])
        if serializer.is_valid():
            serializer.save(location=location)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def department_detail(request, pk):
    try:
        item = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response(status=400)

    if request.method == 'GET':
        serializer = DepartmentSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DepartmentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)

@api_view(['GET'])
def department_rel(request, pk):
    if request.method == 'GET':
        try:
            item = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
               return Response(status=400)
        items = Category.objects.filter(department=item).all()
        serializer = CategorySerializer(items, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        items = Category.objects.all()
        serializer = CategorySerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        department = Department.objects.get(id=request.data['department'])
        if serializer.is_valid():
            serializer.save(department=department)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        item = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=400)

    if request.method == 'GET':
        serializer = CategorySerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)

@api_view(['GET'])
def category_rel(request, pk):
    if request.method == 'GET':
        try:
            item = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
               return Response(status=400)
        items = Subcategory.objects.filter(category=item).all()
        serializer = SubcategorySerializer(items, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def subcategory_list(request):
    if request.method == 'GET':
        items = Subcategory.objects.all()
        serializer = SubcategorySerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubcategorySerializer(data=request.data)
        category = Category.objects.get(id=request.data['category'])
        if serializer.is_valid():
            serializer.save(category=category)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def subcategory_detail(request, pk):
    try:
        item = Subcategory.objects.get(pk=pk)
    except Subcategory.DoesNotExist:
        return Response(status=400)

    if request.method == 'GET':
        serializer = SubcategorySerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubcategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)

@api_view(['GET'])
def subcategory_rel(request, pk):
    if request.method == 'GET':
        try:
            item = Subcategory.objects.get(pk=pk)
        except Subcategory.DoesNotExist:
               return Response(status=400)
        items = FlatData.objects.filter(subcategory=item).all()
        serializer = FlatDataSerializer(items, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def flatdata_list(request):
    if request.method == 'GET':
        items = FlatData.objects.all()
        serializer = FlatDataSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FlatDataSerializer(data=request.data)
        subcategory = Subcategory.objects.get(id=request.data['subcategory'])
        if serializer.is_valid():
            serializer.save(subcategory=subcategory)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def flatdata_detail(request, pk):
    try:
        item = FlatData.objects.get(pk=pk)
    except FlatData.DoesNotExist:
        return Response(status=400)

    if request.method == 'GET':
        serializer = FlatDataSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FlatDataSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)

@api_view(['POST'])
def import_data(request):
    if request.method == 'POST':
       if 'file' in request.data:
            locations = []
            departments = []
            categories = []
            subcategories = []
            l1 = csv.reader(request.data['file'], delimiter=',', quoting=csv.QUOTE_MINIMAL, escapechar = '\\')
            for row in l1:
                if row[0] == 'SKU':
                   continue 
                lt = unicode(row[2], errors='ignore')
                dt = unicode(row[3], errors='ignore')
                ct = unicode(row[4], errors='ignore')
                st = unicode(row[5], errors='ignore')
                if lt not in locations:
                   serializer = LocationSerializer(data={'name':lt})
                   if serializer.is_valid():
                      serializer.save()
                      lid = serializer.data['id']
                      serializer = DepartmentSerializer(data={'name':dt})
                      if serializer.is_valid():
                         serializer.save(location=Location.objects.get(id=lid))
                         did = serializer.data['id']
                         serializer = CategorySerializer(data={'name':ct})
                         if serializer.is_valid():
                            serializer.save(department=Department.objects.get(id=did))
                            cid = serializer.data['id']
                            serializer = SubcategorySerializer(data={'name':st})
                            if serializer.is_valid():
                               serializer.save(category=Category.objects.get(id=cid))
                               sid = serializer.data['id']
                               locations.append(lt)
                               departments.append(dt)
                               categories.append(ct)
                               subcategories.append(st)
                elif dt not in departments:
                     serializer = DepartmentSerializer(data={'name':dt})
                     if serializer.is_valid():
                        serializer.save(location=Location.objects.get(name=lt))
                        did = serializer.data['id']
                        serializer = CategorySerializer(data={'name':ct})
                        if serializer.is_valid():
                           serializer.save(department=Department.objects.get(id=did))
                           cid = serializer.data['id']
                           serializer = SubcategorySerializer(data={'name':st})
                           if serializer.is_valid():
                              serializer.save(category=Category.objects.get(id=cid))
                              sid = serializer.data['id']
                              departments.append(dt)
                              categories.append(ct)
                              subcategories.append(st)
                elif ct not in categories:
                     serializer = CategorySerializer(data={'name':ct})
                     if serializer.is_valid():
                        serializer.save(department=Department.objects.get(name=dt))
                        cid = serializer.data['id']
                        serializer = SubcategorySerializer(data={'name':st})
                        if serializer.is_valid():
                           serializer.save(category=Category.objects.get(id=cid))
                           sid = serializer.data['id']
                           categories.append(ct)
                           subcategories.append(st)
                elif st not in subcategories:
                     serializer = SubcategorySerializer(data={'name':st})
                     if serializer.is_valid():
                        serializer.save(category=Category.objects.get(name=ct))
                        sid = serializer.data['id']
                        subcategories.append(st)
                else:
                     sid = Subcategory.objects.get(name=st).id
                
                serializer = FlatDataSerializer(data={'name':row[1]})
                if serializer.is_valid():
                   serializer.save(subcategory=Subcategory.objects.get(id=sid))

            return Response(status=204)
    return Response("Pass file to import",status=400) 

