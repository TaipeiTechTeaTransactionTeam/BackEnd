from .models import ProductDiscount
class ProductDiscountItem:
    def __init__(self,product,discount):
        self.product=product
        self.discount=discount
    def __getattr__(self,name):
        if name=="isDiscount" or name=="haveDiscount":
            return self.discount!=0
        if name=="price" or name=="finalPrice":
            return self.originPrice-self.discount
        if name=="originPrice":
            return self.product.price
        if name=="imgurl":
            return self.product.image.url
        if name=="image" :
            return self.product.image
        if name=="id":
            return self.product.id
        if name=="name":
            return self.product.name
        if name=="amount":
            return self.product.amount
        if name=="isSoldout":
            return self.product.amount==0
    def __str__(self):
        return self.product.name
def getProductDiscountList(productList):
    pDiscounts = list(ProductDiscount.objects.filter(product__in=[x.id for x in productList]).all())
    products=[]
    for p in productList:
        products.append(ProductDiscountItem(p,next((x.discount for x in pDiscounts if p.id==x.product.id),0)))
    return products