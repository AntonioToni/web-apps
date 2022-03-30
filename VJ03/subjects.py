from http import cookies
import os

subjects = {
    'ip' : { 'name' : 'Introduction to programming' , 'year' : 1, 'ects' : 6 },
    'c1' : { 'name' : 'Calculus 1' , 'year' : 1, 'ects' : 7 },
    'cu' : { 'name' : 'Computer usage' , 'year' : 1, 'ects' : 5 },
    'dmt' : { 'name' : 'Digital and microprocessor technology', 'year' : 1, 'ects' : 6 },
    'db' : { 'name' : 'Databases' , 'year' : 2, 'ects' : 6 },
    'c2' : { 'name' : 'Calculus 2' , 'year' : 2, 'ects' : 7 },
    'dsa' : { 'name' : 'Data structures and alghoritms' , 'year' : 2, 'ects' : 5 },
    'ca' : { 'name' : 'Computer architecture', 'year' : 2, 'ects' : 6 },
    'isd' : { 'name' : 'Information systems design' , 'year' : 3, 'ects' : 5 },
    'c3' : { 'name' : 'Calculus 3' , 'year' : 3, 'ects' : 7 },
    'sa' : { 'name' : 'Server Architecture' , 'year' : 3, 'ects' : 6 },
    'cds' : { 'name' : 'Computer and data security', 'year' : 3, 'ects' : 6 }
    };
        
year_names = {
        1 : '1st Year',
        2 : '2nd Year',
        3 : '3rd Year'
    };

year_ids = {
        '1st Year' : 1,
        '2nd Year' : 2,
        '3rd Year' : 3
};

status_names = {
    'not' : 'Not selected',
    'enr' : 'Enrolled',
    'pass' : 'Passed',
};

def cookie2(dict_key, value_dict_key=None):
    cookies_string = os.environ.get('HTTP_COOKIE', '')
    all_cookies_object = cookies.SimpleCookie(cookies_string)
    if value_dict_key is not None:
        cookie = cookies.SimpleCookie()
        cookie[dict_key] = value_dict_key
        print(cookie.output())
    elif all_cookies_object.get(dict_key):
        value_dict_key = all_cookies_object.get(dict_key).value
    else:
        value_dict_key = 'not'
    return value_dict_key
