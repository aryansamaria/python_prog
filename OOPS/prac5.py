class Order:
    product={'a':2500,'b':2000,'c':5000,'d':5000}
    def __init__(self,oid,cn,*args):
        self.product=args
        self.odid=oid
        self.cname=cn
    def add_order(self):
        pr=Order.get_value()
        if pr in Order.product.keys():
                



        