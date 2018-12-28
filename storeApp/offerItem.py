class OfferItem:
    def __init__(self,offer,discount):
        self.offer=offer
        self.discount=discount
        self.finalPrice=offer.price-discount
        self.originPrice=self.offer.price
    
