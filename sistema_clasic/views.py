from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from sistema_clasic.models import mdlMain
from .forms import frmCreateCn, frmCreateSt, frmLoadSt

def tablesjoin(request):
    cursor = connection.cursor()
    strSql = ' SELECT country.id, country.Cname, state.Sname FROM country '
    strSql += 'JOIN state ON country.id = state.idCountry;'
    print(strSql)
    cursor.execute(strSql)
    results = cursor.fetchall()
    return render(request, 'index.html', {'mdlMain':results})

def crear_pais(request):
    errores = ""
    idRes = 0
    formulario = frmCreateCn(request.POST or None, request.FILES or None)
    if request.method =='POST':
        new_name = request.POST.get('Cname', None)
    
    if formulario.is_valid():
        try:
            with connection.cursor() as cursor:
                strSql = ' INSERT INTO country '
                strSql += '(id, Cname)'
                strSql += " VALUES (null, '%s')" % (new_name)
                print(strSql)
                cursor.execute(strSql)
                cursor.execute("SELECT MAX(id) FROM country")
                idRes = cursor.fetchone()
                strMsg = "El país " + new_name+ "(" + str(idRes[0]) + ")" + " fue creado exitosamente!"
                messages.success(request, strMsg)
        except Exception as err:
            messages.error(request, err)
        return  render(request, 'crear_pais.html')
    else:
        if(len(formulario.errors)>0):
            errores = formulario.errors.as_json()
            messages.error(request, errores)
    return render(request, 'crear_pais.html')

def crear_estado(request):
    errores = ""
    idRes = 0

    formulario = frmCreateSt(request.POST or None, request.FILES or None)
    print(request.POST)

    if request.method =='POST':
        ed_id = request.POST.get('idCountry', None)
        ed_name = request.POST.get('Sname', None)
    else:
        with connection.cursor() as new_curs:
            new_curs.execute("SELECT * FROM country ORDER BY id ASC")
            countrys = new_curs.fetchall()
    
    if formulario.is_valid():
        try:
            with connection.cursor() as cursor:
                strSql = ' INSERT INTO state '
                strSql += '(id, Sname, idCountry)'
                strSql += " VALUES (null, '%s', '%s')" % (ed_name, ed_id)
                print(strSql)
                cursor.execute(strSql)
                cursor.execute("SELECT MAX(id) FROM state")
                idRes = cursor.fetchone()
                strMsg = "El estado " + ed_name + "(" + str(idRes[0]) + ")" + " fue creado exitosamente!"
                messages.success(request, strMsg)
        except Exception as err:
            messages.error(request, err)
        return  render(request, 'crear_estado.html')
    else:
        if(len(formulario.errors)>0):
            errores = formulario.errors.as_json()
            messages.error(request, errores)
    print(type(countrys))
    return render(request, 'crear_estado.html', {'select_country': countrys})

def cargar_estado(request):
    print("<-- cargar_estado -->")
    strMsg = ""
    errores = ""

    formulario = frmLoadSt(request.POST or None, request.FILES or None)
    print(request.POST)

    if request.method =='POST':
        idCountry = request.POST.get('idCountry', None)
        Sname = request.POST.get('Sname', None)
        Cname = request.POST.get('Cname', None)
        opEdit = request.POST.get('EditState', None)
        opDel = request.POST.get('DeleteState', None)
    
    with connection.cursor() as new_curs:
        new_curs.execute("SELECT * FROM country ORDER BY id ASC")
        countrys = new_curs.fetchall()
    
    if formulario.is_valid():
        return render(request, 'cargar_estado.html', {
            'select_country': countrys,
            'idCountry': idCountry,
            'Sname': Sname,
            'Cname': Cname,
            'inEdit': opEdit,
            'inDel': opDel, 
            'inConfirm': True
        })
    else:
        if(len(formulario.errors)>0):
            errores = formulario.errors.as_json()
            messages.error(request, errores)
    print(type(countrys))
    return render(request, 'cargar_estado.html', {
        'select_country': countrys,
        'idCountry': idCountry,
        'Sname': Sname,
        'Cname': Cname,
        'inEdit': opEdit,
        'inDel': opDel,
        'inConfirm': False
    })

def editar_estado(request):
    print("<-- editar_estado -->")
    strMsg = ""
    strSql = ""

    print(request.POST)
    if request.method =='POST':
        idCountry = request.POST.get('idCountry', None)
        Sname = request.POST.get('Sname', None)
        oldName = request.POST.get('oldName', None)
        opEdit = request.POST.get('EditState', None)
        opDel = request.POST.get('DeleteState', None)
    
    print(str(opEdit) + "-" + str(opDel))
    if(opEdit == "1"):
        try:
            with connection.cursor() as cursor:
                strSql = "SELECT id FROM state WHERE Sname = '%s'" % oldName
                cursor.execute(strSql)
                idRes = cursor.fetchone()
                print(strSql)

                strSql = ' UPDATE state'
                strSql += " SET Sname='%s', idCountry='%s'" % (Sname, idCountry)
                strSql += " WHERE id='%s'" % (str(idRes[0]))
                cursor.execute(strSql)
                print(strSql)
                
                strMsg = "El estado fue actualizado."
                messages.success(request, strMsg)
                return redirect('inicio')
        except Exception as err:
            print(err)
            messages.error(request, err)
    else:
        if(opDel == "1"):
            try:
                with connection.cursor() as cursor:
                    strSql = "SELECT id FROM state WHERE Sname = '%s'" % oldName
                    cursor.execute(strSql)
                    idRes = cursor.fetchone()
                    print(strSql)

                    strSql = ' DELETE FROM state'
                    strSql += " WHERE id='%s'" % (str(idRes[0]))
                    cursor.execute(strSql)
                    print(strSql)
                    
                    strMsg = "El estado fue eliminado."
                    messages.success(request, strMsg)
                    return redirect('inicio')
            except Exception as err:
                messages.error(request, err)

    cursor = connection.cursor()
    strSql = ' SELECT country.id, country.Cname, state.Sname FROM country '
    strSql += 'JOIN state ON country.id = state.idCountry;'
    print(strSql)
    cursor.execute(strSql)
    results = cursor.fetchall()
    return render(request, 'index.html', {'mdlMain':results})
