from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
	response_dict = {'bg_color': '#bc2131'}
	return response_dict

@view_config(route_name='color', renderer='templates/mytemplate.jinja2')
def my_view_color(request):
	mydict = request.matchdict
	response_dict = {'color': mydict['query'],'bg_color': '#bc2131'}
	return response_dict

@view_config(route_name='form', renderer='templates/newtemplate.jinja2')
def my_view_form(request):
	return {'project': 'Lab6'}

@view_config(request_method='POST', route_name='form_bg', renderer='templates/mytemplate.jinja2')
def my_view_form_bg(request):
	print request.POST['bg_color']
	return {'bg_color': request.POST['bg_color']}
