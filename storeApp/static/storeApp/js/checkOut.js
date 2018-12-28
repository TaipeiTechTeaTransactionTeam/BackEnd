import {Uti} from "./Nawauti.js";
/**
 * @function isDebug
 * 在網址後方加入#debug 判斷為True
 * 
 */

var Nawa=Nawa||{};
Nawa.Class=Nawa.Class||{};
/*
  採用miniCart標準
  amount = 價格
  quantity = 數量
  total = 單項總價
 */
Nawa.Class.DisplayObject=
class DisplayObject
{
    constructor(para)
    {
        if(typeof para==="undefined")
            return;
        var cname=para.constructor.name
        if(cname==="String")
            this.fromQueryString(para);
        else if(cname.includes("HTML")&&cname.includes("Element"))
            this.fromHtmlElement(para);
    }
    fromHtmlElement(ele){this.display=ele;}
    fromQueryString(str){this.display=document.querySelector(str);}
    get classList(){return this.display.classList;}
    get innerHTML(){return this.html;}
    set innerHTML(val){this.html=val;}
    get html(){return this.display.innerHTML;}
    set html(val){this.display.innerHTML=val;}
    get innerText(){return this.text;}
    set innerText(val){this.text=val;}
    get text(){return this.display.innerText;}
    set text(val){this.display.innerText=val;}
    set visible(val){if(val!==this.visible){if(val){this.display.classList.remove("d-none");}else {this.display.classList.add("d-none"); }}}
    get visible(){return !this.display.classList.contains("d-none");}
    getObj(obj){return (obj.constructor.name.includes("HTML")&&obj.constructor.name.includes("Element"))?obj:(obj.display)?this.getObj(obj.display):undefined;}
    insertBefore(ele,ref){this.display.insertBefore(this.getObj(ele),this.getObj(ref));}
    insertAfter(ele,ref){this.display.insertAfter(this.getObj(ele),this.getObj(ref));}
    show(){this.visible=true;}
    hide(){this.visible=false;}
    remove(){this.display.remove();}
    append(obj){this.display.append(obj.display||obj);}
    appendTo(father){if(father.display){father.display.append(this.display);}else{father.append(this.display);}}
    prepend(obj){this.display.prepend(obj.display||obj);}
    prependTo(father){if(father.display){father.display.prepend(this.display);}else{father.prepend(this.display);}}
}
/**
 * 結算總管物件
 * @Class CheckOut
 *  
 */
Nawa.Class.CheckOut=
class CheckOut
{
    constructor(cart)
    {
        this.cart=cart;
        this.cartTable=new Nawa.Class.ShoppingCartTable();
        this.checkoutList=new Nawa.Class.CheckOutList(cart);
        this.layoutSetup();
        this.checkoutList.update();
        this.productItems=[];
        for(var cartItem of this.items)
        {
            this.append(cartItem);
        }
        this.cart.on("remove",this.onRemove,this);
        this.cart.on("checkout",this.onCheckout,this);
        this.onViewsChange();
    }
    postTo(path=".")
    {
        var items=[];
        var form=document.createElement("form");
        form.action=path;
        form.method="post";
        for(var item of this.items)
        {
            var newItem={uid:item.get("uid"),quantity:item.get("quantity")}
            items.push(newItem);
        }
        form.innerHTML+=`<input name="items" value='${JSON.stringify(items)}' type="hidden" >`;
        form.innerHTML+=`<input name="eventDiscount" value='${JSON.stringify(this.eventDiscountSrcObject)}' type="hidden" >`;//testing
        var value=document.querySelector(".modal-dialog #addressInput").value;
        form.innerHTML+=`<input name="address" value='${value}' type="hidden">`;
        form.style.display="none";
        form.innerHTML+=csrf;
        document.body.append(form);
        form.submit();
    }
    onCheckout()
    {
        this.postTo();
    }
    onRemove()
    {
        this.onChange();
        this.onViewsChange();
    }
    onAdd()
    {
        this.onChange();
        this.onViewsChange();
    }
    onChange()
    {
        this.checkoutList.update();
    }
    onViewsChange()
    {
        if(this.items.length==0)
        {
            this.checkoutList.hide();
            this.couponSection.hide();
            this.cartTable.hide();
        }
            
        if(this.items.length>=1)
        {
            this.checkoutList.show();
            this.couponSection.show();
            this.cartTable.show();
        }
            
    }

    append(cartItem)
    {
       // i=typeof i === "undefined"?this.number:i;
        var product=new Nawa.Class.CheckOutProduct(cartItem,new Nawa.Class.ProductCartView(cartItem/*,this.number*/),new Nawa.Class.ProductCheckView(cartItem));
        product.closeOnclick=(sender)=>{this.removeItem(sender);sender.cartView.remove();sender.checkView.remove();}
        product.onChange=()=>this.onChange();
        this.productItems.push(product);
        this.cartTable.display.append(product.cartView.display);
        this.checkoutList.append(product.checkView.display);
        this.onViewsChange();
    }
    layoutSetup()
    {
        this.rigthDisplay=new Nawa.Class.DisplayObject(".checkout-right");
        this.rigthDisplay.html="";
        this.leftDisplay=new Nawa.Class.DisplayObject(".checkout-left");
        this.couponSection=new Nawa.Class.DisplayObject(".couponSection");
        this.rigthDisplay.append(this.cartTable.display);
        this.rigthDisplay.append(this.cartTable.emptyDisplay);
        this.leftDisplay.prepend(this.checkoutList.display);
    }
    removeItem(item)
    {
        if(typeof item==="undefined")return;
        switch(item.constructor.name)
        {
            case "CheckOutProduct":
                item=item.cartItem;
            break;
            case "c":
            default:
        }
        this.cart.remove(this.items.indexOf(item));
    }
    get items()
    {
        return this.cart.items();
    }
    get eventDiscountSrcObject(){return window.eventDiscount;}
}
/**
 * 購物車表格
 */
Nawa.Class.ShoppingCartTable=
class ShoppingCartTable extends Nawa.Class.DisplayObject
{
    constructor()
    {
        super();
        this.createElements();
        this.display.classList.add("timetable_sub");
        this.emptyText=`
        <div class="text-center d-flex justify-content-center flex-column">
            <div><img src='/static/base/images/cartEmpty.png'></img></div>    
            <h4 class="my-2">購物車竟然是空的</h4>
            <small class="text-muted">再忙，也要記得買點什麼犒賞自己～</small>
        </div>
        `
        this.hide();
    }
    createElements()
    {
        this.display=document.createElement("table");
        this.display.innerHTML=
        `<thead>
            <tr>	
                <th>商品</th>
                <th>數量</th>
                <th>商品名稱</th>
                <th>價格</th>
                <th>刪除</th>
            </tr>
        </thead>`;
        this.display.append(this.bodyDisplay=document.createElement("tbody"));
        this.emptyDisplay=document.createElement("div");
    }
    set emptyText(val) {this.emptyDisplay.innerHTML=val;}
    get emptyText() {return this.emptyDisplay.innerHTML;}
    set visible(val)
    {
        if(val!==this.visible)
        {
            if(val)
            {
                this.display.classList.remove("d-none");
                this.emptyDisplay.classList.add("d-none");
            }
            else
            {
                this.display.classList.add("d-none");
                this.emptyDisplay.classList.remove("d-none");
            }
        }
    }
    get visible(){return !this.display.classList.contains("d-none");}
}
/**
 * 結算清單的列表Html管理物件
 */
Nawa.Class.CheckOutList=
class CheckOutList extends Nawa.Class.DisplayObject
{
    constructor(cart)
    {
        super();
        this.cart=cart;
        this.createObjects();
        this.createElements();
        this.display.classList.add("checkout-left-basket");
        this.title="結算";

    }
    createObjects()
    {
        this.subtotalObject=new Nawa.Class.ProductCheckView({name:"小結",total:0});
        this.subtotalObject.display.classList.add("subtotal");
        this.eventDiscountObject=new Nawa.Class.ProductCheckView({name:"活動折扣",total:0})
        this.eventDiscountObject.classList.add("discount","eventDiscount");
        this.shippingObject=new Nawa.Class.ProductCheckView({name:"運費",total:this.shippingPrice||0});
        this.totalObject=new Nawa.Class.ProductCheckView({name:"總額",total:0});
    }
    get shippingPrice(){return shippingPrice||0-this.shippingDiscountValue;}
    set shippingPrice(val){this.shippingObject.total=val;}

    get shippingDiscountSrcObject(){return shippingDiscount;}
    get shippingDiscount(){return this.shippingDiscountSrcObject.discount;}
    get shippingDiscountCondition(){return this.shippingDiscountSrcObject.condition;}
    get shippingDiscountValue(){return Math.floor
        (
            typeof this.shippingDiscountSrcObject!=="undefined"?
            (
                this.totalWithoutShippingPrice>=this.shippingDiscountCondition?
                (
                    this.shippingDiscount>=1?
                    (
                        this.shippingDiscount>=shippingPrice?
                            shippingPrice
                        :
                            this.shippingDiscount
                    ):
                        shippingPrice*(1-this.shippingDiscount)
                ):
                    0
            ):
           0
        );
    }

    get totalWithoutShippingPrice(){return this.subtotal+this.eventDiscountValue;}
    
    get subtotal(){return this.cart.total();}
    set subtotal(val){this.subtotalObject.total=val;}

    get eventDiscount(){return this.eventDiscountSrcObject.discount;}
    get eventDiscountSrcObject(){return window.eventDiscount;}
    set eventDiscount(val){this.eventDiscountObject.total=val;}
    get eventDiscountCondition(){return this.eventDiscountSrcObject.condition;}
    get eventDiscountValue()
    {
        return Math.floor(
                typeof this.eventDiscountSrcObject!=="undefined"&&this.subtotal>=(this.eventDiscountCondition||0)?
                (
                    this.eventDiscount>=1?
                    (
                        this.eventDiscount>this.subtotal?
                            this.subtotal:
                            this.eventDiscount
                    ):
                        this.subtotal*(1-this.eventDiscount)
                ):
                0
            );
    }
    set eventDiscountValue(val){this.eventDiscountObject.total=val;}
    get eventDiscountString(){return (this.eventDiscount>=1?"折價"+this.eventDiscount+"元":(this.eventDiscount*100)%10===0?this.eventDiscount*10+"折":this.eventDiscount*100+"折");}
    set total(val){this.totalObject.total=val;}
    get total()
    {
        this.updateTotal();
        return this.totalObject.total;
    }
    set title(val){this.titleDisplay.innerText=val;}
    get title(){return this.titleDisplay.innerText;}
    updateDiscount(){this.eventDiscount=this.eventDiscountValue;}
    updateShipping(){this.shippingPrice=this.shippingPrice;}
    updateTotal()
    {
        this.subtotal=this.subtotal;
        this.total=this.subtotal+this.shippingPrice-this.eventDiscountValue;
    }
    update()
    {
        this.updateDiscount();
        this.updateShipping();
        this.updateTotal();
    }
    append(display){this.listDisplay.insertBefore(display,this.subtotalObject.display);}
    createElements()
    {
        this.display=document.createElement("div");
        this.display.append
        (
            (this.titleDisplay=new Nawa.Class.DisplayObject(document.createElement("h4"))).display,
            (this.listDisplay=new Nawa.Class.DisplayObject(document.createElement("ul"))).display
        );
        this.listDisplay.append(this.subtotalObject.display);
        this.listDisplay.append(this.shippingObject.display);
        this.listDisplay.append(this.eventDiscountObject);
        this.listDisplay.append(this.totalObject.display);
    }
    
}
/**
 * 單個物品的關聯、處理(model)
 */
Nawa.Class.CheckOutProduct=
class CheckOutProduct
{
    constructor(cartItem,cartView,checkView)
    {
        this.cartItem=cartItem;
        this.cartView=cartView;
        this.checkView=checkView;
        this.updateStock();
        this.cartItem.on("change",()=>{this.onChange();this.updateViews();});
        this.cartView.closeOnclick=()=>{this.closeOnclick(this);}
        this.cartView.plusOnclick=()=>
        {

            if(this.quantity<this.stockQuantity)
            {
                this.quantity++;
            }
            else if(this.quantity>this.stockQuantity)
            {
                this.quantity=this.stockQuantity;
            }
            this.updateButtonStates();
            this.updateStock();
        };
        this.cartView.minusOnclick=()=>
        {
            if(this.quantity>1)
                this.quantity--;
            else
            {
                this.quantity=1;
            }
            this.updateButtonStates();
            this.updateStock();
        }
    }
    updateButtonStates()
    {
        if(this.quantity>=this.stockQuantity)
            this.cartView.plusButton.classList.add("disabled");
        else 
            this.cartView.plusButton.classList.remove("disabled");
        if(this.quantity<=1)
            this.cartView.minusButton.classList.add("disabled");
        else 
            this.cartView.minusButton.classList.remove("disabled");
    }
    async updateStock(){
        this.stockQuantity=await Uti.productQuantity(this.uid);
    }
    closeOnclick(product){}
    onChange(){}
    removeViews()
    {
        this.cartView.remove();
        this.checkView.remove();
    }
    updateViews()
    {
        this.cartView.attrFromCartItem(this.cartItem);
        this.checkView.attrFromCartItem(this.cartItem);
    }
    set stockQuantity(val){this._stock=val;}
    get stockQuantity(){return this._stock;}
    get uid(){return parseInt(this.cartItem.get("uid"));}
    set quantity(val)
    {this.cartItem.set("quantity",val);}
    get quantity(){return this.cartItem.get("quantity");}
}
/**
 * @class ProductCartView
 * 作為checkout頁面上方列表中一個tuple所有html Element的管理物件
 */
Nawa.Class.ProductCartView=
class ProductCartView
{
    constructor(cartItem,/*number,*/moneySymbol="NT$")
    {
        this.createFields();
        this.addClasses();
        this.moneySymbol=moneySymbol;
        this.addEventListeners();
        this.attrFromCartItem(cartItem);
        //this.number=number||1;
    }
    attrFromCartItem(cartItem)
    {
        if(typeof cartItem==="undefined")
            return;
        this.name=cartItem.get("item_name")||"no name";
        this.quantity=cartItem.get("quantity")||"1";
        this.imgSrc=cartItem.get("imgSrc");
        this.amount=cartItem.total();
    }
    addEventListeners()
    {
        this.plusButton.addEventListener("click",()=>this.plusOnclick());
        this.minusButton.addEventListener("click",()=>this.minusOnclick());
        this.closeButton.addEventListener("click",()=>{this.closeOnclick()});
    }
    plusOnclick(){}
    minusOnclick(){}
    closeOnclick(){}
    createFields()
    {
        this.display=document.createElement("tr");
        this.display.append
        (
           // this.numField=document.createElement("td"),
            this.createImageField(),
            this.createQuantityField(),
            this.nameField=document.createElement("td"),
            this.amoutField=document.createElement("td"),
            this.createCloseField()
        );
    }
    addClasses()
    {
        for(var td of this.display.cells)
            td.classList.add("invert");
        this.addImageClass();
        this.addQuantityClass();
        this.addCloseClass();
    }
    createQuantityField()
    {
        this.quantityField=document.createElement("td");
        var quantitySelect=document.createElement("div");
        this.minusButton=document.createElement("div");
        this.quantityDisplay=document.createElement("div");
        this.plusButton=document.createElement("div");
        this.quantityField.append(quantitySelect);
        quantitySelect.append(this.minusButton,this.quantityDisplay,this.plusButton);
        return this.quantityField;
    }
    addQuantityClass()
    {
        this.quantityField.querySelector("div").classList.add("quantity-select");
        this.minusButton.classList.add("entry","value-minus","btn");
        this.plusButton.classList.add("entry","value-plus","btn");
        this.quantityDisplay.classList.add("entry","value");
    }
    createImageField()
    {
        this.imageField=document.createElement("td");
        this.imageField.append(this.imageLink=document.createElement("a"));
        this.imageLink.append(this.image=document.createElement("img"));
        return this.imageField;
    }
    addImageClass()
    {
        this.imageField.classList.remove("invert");
        this.imageField.classList.add("invert-image");
        this.image.classList.add("img-responsive");
    }
    createCloseField()
    {
        this.closeField=document.createElement("td");
        var container=document.createElement("div");
        this.closeField.append(container);
        container.append(this.closeButton=document.createElement("div"));
        return this.closeField;
    }
    addCloseClass()
    {
        this.closeField.querySelector("div").classList.add("rem");
        this.closeButton.classList.add("closeBtn");
    }
    set imgSrc(val) {this.image.src=val;}
    get imgSrc(){return this.image.src;}
    set imgLink(val){this.imageLink.href=val;}
    get imgLink(){return this.imageLink.href;}
    set quantity(val){this.quantityDisplay.innerText=val>0?val:this.quantityDisplay.innerText;}
    get quantity(){return parseInt(this.quantityDisplay.innerText);}
    set amount(val)
    {
        this._amount=val;
        this.amoutField.innerText=this.moneySymbol+val;
    }
    get amount(){return parseFloat(this._amount);}
    set name(val){ this.nameField.innerText=val;}
    get name(){return this.nameField.innerText; }
    remove() {this.display.remove();}
}
/**
 * @class ProductCheckView
 * 結算清單中每個項目的Html管理物件
 */
Nawa.Class.ProductCheckView=
class ProductCheckView extends Nawa.Class.DisplayObject
{
    constructor(inputItem,moneySymbol="NT$")
    {
        super();
        this.moneySymbol=moneySymbol;
        this.createElements();
        this.attrFromInputItem(inputItem);
    }
    attrInput(name,total)
    {
        this.name=name||"no name";
        this.total=total||0;
    }
    attrFromInputItem(inputItem)
    {
        if(typeof inputItem=="undefined")
            return;
        if(inputItem.constructor.name==="c")//inputCartItem
            this.attrFromCartItem(inputItem);
        if(inputItem.name)
            this.attrInput(inputItem.name,inputItem.total);
    }
    attrFromCartItem(cartItem)
    {
        if(typeof cartItem==="undefined")
            return;
        this.attrInput(cartItem.get("item_name"),cartItem.total());
    }
    createElements()
    {
        this.display=document.createElement("li");
        var i=document.createElement("i");
        i.innerText='-';
        this.display.append
        (
            this.nameDisplay=document.createTextNode(""),
            i,
            this.totalDisplay=document.createElement("span")
        );
    }
    get name(){return this.nameDisplay.data;}
    set name(val){this.nameDisplay.data=val;}
    get total(){return this._total;}
    set total(val)
    {
        this._total=val;
        this.totalDisplay.innerText=this.moneySymbol+val;
    }
}

$(
    ()=>
    {
        var checkOut=new Nawa.Class.CheckOut(paypal.minicart.cart);
        $(".checkout.btn").on("click",function()
        {
            if(!isLogged)
                location.replace("/login");
        })
        $(".modal-dialog #modalConfirm").on("click",function()
        {

            var addressInput=document.querySelector(".modal-dialog #addressInput");
            if(addressInput.value==="")
            {
                alert("欄位不能為空");
                return;
            }
            if(addressInput.value.length<8)
            {
                alert("地址欄位不小於8");
                return;
            }
            if(!Uti.isDebug())
            {
                checkOut.cart.destroy();
            }
                
            checkOut.postTo();

        })
        function updateEventDiscountToWindow()
        {
            window.eventDiscount=window.eventDiscounts[this.selectedIndex];
            checkOut.onChange();
        }
        $("#inputGroupCoupon").on("change",updateEventDiscountToWindow);
    }
);

