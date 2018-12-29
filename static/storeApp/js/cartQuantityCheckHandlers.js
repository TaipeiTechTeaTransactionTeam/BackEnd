import {Uti} from "./Nawauti.js";
$(()=>
{
    async function updateStock(item)
    {
        item.stock=await Uti.productQuantity(parseInt(item.get("uid")));
    }
    function quantityCheck()
    {
        if(this.get("quantity")>this.stock)
            this.set("quantity",this.stock);
        updateStock(this);
    }
    paypal.minicart.cart.on("add",
    function(id,item,isExist)
    {
        if(!isExist)
            item.on("change",quantityCheck);
    });
    for(var item of paypal.minicart.cart.items())
    {
        updateStock(item);
        item.on("change",quantityCheck);
    }
});