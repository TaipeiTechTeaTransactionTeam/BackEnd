export var Uti=Uti||{};
Uti.productQuantity=
function productQuantity(id)
{
    if($)
        return $.get("/productQuantity/"+JSON.stringify(id))
      
    console.warn("JQuery are needed");
    return val;
};
