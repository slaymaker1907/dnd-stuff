import pystache

def make_template():
    with open('ability_score.mustache') as f:
        template = f.read()
    attributes = ['Strength', 'Dexterity', 'Constitution', 'Intellect', 'Wisdom', 'Charisma']
    lst = [{'name':name} for name in attributes]
    lst[-1]['last'] = True
    with open('ability_score.html', 'w') as f:
        f.write(pystache.render(template, {'attributes':lst, 'jquery':'jquery-2.2.4.min.js', 'bootstrap':'bootstrap-3.3.6/dist/css/bootstrap.min.css'}))

if __name__ == '__main__':
    make_template()
