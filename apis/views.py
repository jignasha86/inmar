import csv
import logging
import gettext
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apis.models import Location, Department, Category, Subcategory, FlatData
from apis.serializers import LocationSerializer, DepartmentSerializer, CategorySerializer, SubcategorySerializer, FlatDataSerializer

logger = logging.getLogger('django')

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
translate = gettext.translation('handroll', localedir, fallback=True)
_ = translate.gettext

@api_view(['GET', 'POST'])
def location_list(request):
    """
        Location list resource view
    """

    try:
	if request.method == 'GET':
           logger.debug(_("Location list API called"))
	   items = Location.objects.all()
	   serializer = LocationSerializer(items, many=True)
	   return Response(serializer.data)

        elif request.method == 'POST':
	     logger.debug(_("Location create API called"))
	     serializer = LocationSerializer(data=request.data)
             if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data, status=201)
             return Response(serializer.errors, status=400)
    except Exception as ex:
           logger.error(_(ex.message))
           raise ex


@api_view(['GET', 'PUT', 'DELETE'])
def location_detail(request, pk):
    """
        Location detail resource view
    """

    try:
	 try:
	     item = Location.objects.get(pk=pk)
	 except Location.DoesNotExist:
		logger.error(_("Location with id "+pk+" not existing"))
		return Response(status=400)

	 if request.method == 'GET':
	    serializer = LocationSerializer(item)
	    return Response(serializer.data)

	 elif request.method == 'PUT':
	      logger.debug(_("Location update API called"))
	      serializer = LocationSerializer(item, data=request.data)
	      if serializer.is_valid():
		 serializer.save()
		 return Response(serializer.data)
	      return Response(serializer.errors, status=400)

	 elif request.method == 'DELETE':
	      item.delete()
	      return Response(status=204)
    except Exception as ex:
           logger.error(_(ex.message))
           raise ex


@api_view(['GET'])
def location_rel(request, pk):
    """
        Location department relation view
    """

    try:
	 if request.method == 'GET':
	    logger.debug(_("Get list of departments for location id "+pk))
	    try:
		item = Location.objects.get(pk=pk)
	    except Location.DoesNotExist:
		   return Response(status=400)
            items = Department.objects.filter(location=item).all()
	    serializer = DepartmentSerializer(items, many=True)
	    return Response(serializer.data)
    except Exception as ex:
            logger.error(_(ex.message))
            raise ex


@api_view(['GET', 'POST'])
def department_list(request):
    """
        Department list resource view
    """
    try:
        if request.method == 'GET':
           logger.debug(_("Depatment list API called"))
           items = Department.objects.all()
	   serializer = DepartmentSerializer(items, many=True)
	   return Response(serializer.data)

        elif request.method == 'POST':
	     logger.debug(_("Department Create API called"))
	     serializer = DepartmentSerializer(data=request.data)
	     location = Location.objects.get(id=request.data['location'])
	     if serializer.is_valid():
                serializer.save(location=location)
                return Response(serializer.data, status=201)
             return Response(serializer.errors, status=400)
    except Exception as ex:
           logger.error(_(ex.message))
           raise ex


@api_view(['GET', 'PUT', 'DELETE'])
def department_detail(request, pk):
    """
        Department detail resource view
    """

    try:
	try:
	    item = Department.objects.get(pk=pk)
	except Department.DoesNotExist:
	    logger.error(_("Department with id "+pk+" not existing"))
	    return Response(status=400)

	if request.method == 'GET':
	    serializer = DepartmentSerializer(item)
	    return Response(serializer.data)

	elif request.method == 'PUT':
	    logger.debug(_("Department update API called"))
	    serializer = DepartmentSerializer(item, data=request.data)
	    try:
		location = Location.objects.get(id=request.data['location']['id'])
	    except:
		   location = Location.objects.get(id=request.data['location'])

	    if serializer.is_valid():
		serializer.save(location=location)
		return Response(serializer.data)
	    return Response(serializer.errors, status=400)

	elif request.method == 'DELETE':
	    logger.debug(_("Department delete API called"))
	    item.delete()
	    return Response(status=204)
    except Exception as ex:
           logger.error(_(ex.message))
           raise ex 


@api_view(['GET'])
def department_rel(request, pk):
    """
        Department category relation view
    """

    try:
	if request.method == 'GET':
	    logger.debug(_("Get list of categories of department id "+pk))
	    try:
		item = Department.objects.get(pk=pk)
	    except Department.DoesNotExist:
		   return Response(status=400)
	    items = Category.objects.filter(department=item).all()
	    serializer = CategorySerializer(items, many=True)
	    return Response(serializer.data)
    except Exception as ex:
           logger.error(_(ex.message))
           raise ex


@api_view(['GET', 'POST'])
def category_list(request):
    """
        Category list resource view
    """

    try:
	if request.method == 'GET':
	    logger.debug(_("category list API called"))
	    items = Category.objects.all()
	    serializer = CategorySerializer(items, many=True)
	    return Response(serializer.data)

	elif request.method == 'POST':
	    logger.debug(_("Category create API called"))
	    serializer = CategorySerializer(data=request.data)
	    department = Department.objects.get(id=request.data['department'])
	    if serializer.is_valid():
		serializer.save(department=department)
		return Response(serializer.data, status=201)
	    return Response(serializer.errors, status=400)
    except Exception as ex:
            logger.error(_(ex.message))
            raise ex


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    """
        Category detail resource view
    """

    try:
	try:
	    item = Category.objects.get(pk=pk)
	except Category.DoesNotExist:
	    logger.error(_("Category with id "+pk+" not existing"))
	    return Response(status=400)

	if request.method == 'GET':
	    serializer = CategorySerializer(item)
	    return Response(serializer.data)

	elif request.method == 'PUT':
	    logger.debug(_("Category update API called"))
	    serializer = CategorySerializer(item, data=request.data)
	    try:
		department = Department.objects.get(id=request.data['department']['id'])
	    except:
		   department = Department.objects.get(id=request.data['department'])
		 
	    if serializer.is_valid():
		serializer.save(department=department)
		return Response(serializer.data)
	    return Response(serializer.errors, status=400)

	elif request.method == 'DELETE':
	    logger.debug(_("Category delete API called"))
	    item.delete()
	    return Response(status=204)
    except Exception as ex:
            logger.error(_(ex.message))
            raise ex


@api_view(['GET'])
def category_rel(request, pk):
    """
        Category subcategory relation view
    """

    try:
	if request.method == 'GET':
	    logger.debug(_("Get list of subcategories with of category id "+pk))
	    try:
		item = Category.objects.get(pk=pk)
	    except Category.DoesNotExist:
		   return Response(status=400)
	    items = Subcategory.objects.filter(category=item).all()
	    serializer = SubcategorySerializer(items, many=True)
	    return Response(serializer.data)
    except Exception as ex:
            logger.error(_(ex.message))
            raise ex


@api_view(['GET', 'POST'])
def subcategory_list(request):
    """
        Subcategory list resource view
    """

    try:
	if request.method == 'GET':
	    logger.debug(_("Subcategory list API called"))
	    items = Subcategory.objects.all()
	    serializer = SubcategorySerializer(items, many=True)
	    return Response(serializer.data)

	elif request.method == 'POST':
	    logger.debug(_("Subcategory create API called"))
	    serializer = SubcategorySerializer(data=request.data)
	    category = Category.objects.get(id=request.data['category'])
	    if serializer.is_valid():
		serializer.save(category=category)
		return Response(serializer.data, status=201)
	    return Response(serializer.errors, status=400)
    except Exception as ex:
            logger.error(_(ex.message))
            raise ex


@api_view(['GET', 'PUT', 'DELETE'])
def subcategory_detail(request, pk):
    """
        Subcategory details resource view
    """

    try:
	try:
	    item = Subcategory.objects.get(pk=pk)
	except Subcategory.DoesNotExist:
	    logger.error(_("Subcategory with id "+pk+" not existing"))
	    return Response(status=400)

	if request.method == 'GET':
	    serializer = SubcategorySerializer(item)
	    return Response(serializer.data)

	elif request.method == 'PUT':
	    logger.debug(_("Subcategory update API called"))
	    serializer = SubcategorySerializer(item, data=request.data)
	    try:
		category = Category.objects.get(id=request.data['category']['id'])
	    except:
		   category = Category.objects.get(id=request.data['category'])
	    if serializer.is_valid():
		serializer.save(category=category)
		return Response(serializer.data)
	    return Response(serializer.errors, status=400)

	elif request.method == 'DELETE':
	    logger.debug(_("Subcategory delete API called"))
	    item.delete()
	    return Response(status=204)
    except Exception as ex:
            logger.error(_(ex.message))
            raise ex


@api_view(['GET'])
def subcategory_rel(request, pk):
    """
        Subcategory product relation view
    """

    try:
	if request.method == 'GET':
	    logger.debug(_("Get list of all products of subcategory id "+pk))
	    try:
		item = Subcategory.objects.get(pk=pk)
	    except Subcategory.DoesNotExist:
		   return Response(status=400)
	    items = FlatData.objects.filter(subcategory=item).all()
	    serializer = FlatDataSerializer(items, many=True)
	    return Response(serializer.data)
    except Exception as ex:
            logger.error(_(ex.message))
            raise ex


@api_view(['GET', 'POST'])
def flatdata_list(request):
    """
        Product list resource view
    """

    try:
	if request.method == 'GET':
	    logger.debug(_("Product list API called"))
	    items = FlatData.objects.all()
	    serializer = FlatDataSerializer(items, many=True)
	    return Response(serializer.data)

	elif request.method == 'POST':
	    logger.debug(_("Product create API called"))
	    serializer = FlatDataSerializer(data=request.data)
	    subcategory = Subcategory.objects.get(id=request.data['subcategory'])
	    if serializer.is_valid():
		serializer.save(subcategory=subcategory)
		return Response(serializer.data, status=201)
	    return Response(serializer.errors, status=400)
    except Exception as ex:
            logger.error(_(ex.message))
            raise ex


@api_view(['GET', 'PUT', 'DELETE'])
def flatdata_detail(request, pk):
    """
        Product detail resource view
    """

    try:
	try:
	    item = FlatData.objects.get(pk=pk)
	except FlatData.DoesNotExist:
	    logger.error(_("Product with id "+pk+" not existing"))
	    return Response(status=400)

	if request.method == 'GET':
	    serializer = FlatDataSerializer(item)
	    return Response(serializer.data)

	elif request.method == 'PUT':
	    logger.debug(_("Product update API called"))
	    serializer = FlatDataSerializer(item, data=request.data)
	    try:
		subcategory = Subcategory.objects.get(id=request.data['subcategory']['id'])
	    except:
		   subcategory = Subcategory.objects.get(id=request.data['subcategory'])
	    if serializer.is_valid():
		serializer.save(subcategory=subcategory)
		return Response(serializer.data)
	    return Response(serializer.errors, status=400)

	elif request.method == 'DELETE':
	    logger.debug(_("Product delete API called"))
	    item.delete()
	    return Response(status=204)
    except Exception as ex:
           logger.error(_(ex.message))
           raise ex


@api_view(['GET'])
def flare_data(request):
    """
        Get json graph data for all products
    """

    try:
	if request.method == 'GET':
	   logger.debug(_("Get json of all nested data"))
	   output = {"name":"Start","children":[]}
	   lts = Location.objects.all()
	   i = 0
	   for lt in lts:
	       output['children'].append({"name": lt.name, "children": []})
	       x = 0         
	       dts = Department.objects.filter(location=lt).all()
	       for dt in dts:
		   output['children'][i]["children"].append({"name": dt.name, "children": []})
		   y = 0
		   cts = Category.objects.filter(department=dt).all()           
		   for ct in cts:
		       output['children'][i]["children"][x]["children"].append({"name": ct.name, "children": []})
		       z = 0
		       sts = Subcategory.objects.filter(category=ct).all()
		       for st in sts:
			   output['children'][i]["children"][x]["children"][y]["children"].append({"name": st.name, "children": []})
			   items = FlatData.objects.filter(subcategory=st).all()
			   for item in items:
			       output['children'][i]["children"][x]["children"][y]["children"]\
			       [z]["children"].append({"name": item.name, "children": []})   
			   z = z + 1
		       y = y + 1
		   x = x + 1
	       i = i + 1
	   return Response(output)
    except Exception as ex:
            logger.error(_(ex.message))
            raise ex


@api_view(['POST'])
def import_data(request):
    """
        Import data in database from csv file
    """

    try:
	if request.method == 'POST':
	   logger.debug(_("Import data from csv file called"))
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
    except Exception as ex:
           logger.error(_(ex.message))
           raise ex
