import random
import string
from django.utils.text import slugify

def random_string_generator(size=10,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



# above return statement is as follows its called code  comprehensive
    # s=''
    # for i in range(size):
    #     r=random.choice(chars)
    #     s=s+r
    # return s
def unique_order_id(instance):
    order_new_id=random_string_generator()
    Klass=instance.__class__
    qs_exists=Klass.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return unique_order_id(instance)
    return order_new_id
    


def unique_slug_generator(instance,new_slug=None):
    
    if new_slug is not None:
        #this condition True when function called recursively
        slug=new_slug
    elif instance.slug is not None:
        #This condition True when user enter some value in slug field
        slug=slugify(instance.slug)
    else:
        #this True when user Not Enter any value
        slug=slugify(instance.pname)

    Klass=instance.__class__  #this gives the class object for which this is created
    qs_exists=Klass.objects.filter(slug=slug).exclude(id=instance.id).exists()#here exclude is use not "!=" operator
    print(qs_exists)
    if qs_exists:
        #above condition check that the new_slug which is generate is already present or not at different id is it is present then function call recursively

        new_slug="{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )

        return unique_slug_generator(instance,new_slug=new_slug)
    return slug