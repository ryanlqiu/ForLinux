def story(x,y=0,*z):
    print(x,y,z)
def goodstory(**kwg):
    return 'Had %(name)s not seen the sun, I could have %(verb)s shade.'% kwg
    
A={'name':'I','verb':'borne'}
