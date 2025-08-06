

def check_read_articles(request):
    try:
        read_articles = request.session['read_articles']
    except:
        request.session['read_articles'] = []
        read_articles = request.session.get('read_articles')
    return read_articles


def check_ratings(request):
    try:
        done_ratings = request.session['done_ratings']
    except:
        request.session['done_ratings'] = []
        done_ratings = request.session.get('done_ratings')
    return done_ratings