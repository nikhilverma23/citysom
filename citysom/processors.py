def template_data(request):
    
    message = request.session.get('message')
    if message:
        del request.session['message']
        
    error = request.session.get('error')
    if error:
        del request.session['error']
    
    city = request.session.get('city')
      
    return {
            'message' : message,
            'error' : error,
            'city' : city
        }