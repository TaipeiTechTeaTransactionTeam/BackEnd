$(
    function()
    {
        function getPrice(productContainer)
        {
            var originPrice=productContainer.querySelector(".snipcart-details input[name='amount']").value;
            var discountInput=productContainer.querySelector(".snipcart-details input[name='discount_amount']")
            var discount=(discountInput)?discountInput.value:0;
            return originPrice-discount;
        }
        var container=document.querySelector(".products-right");
        var productContainers=Array.from(container.querySelectorAll(".top_brand_left.agile_top_brands_grids"));
        function ascCmp(a,b)
        {
            if(getPrice(a)<getPrice(b))
                return -1;
            else if(getPrice(a)>getPrice(b))
                return 1;
            return 0;
        }
        function descCmp(a,b)
        {
            return ascCmp(b,a);
        }
        function resetContainer(containers)
        {
            container.innerHTML="";
            for(var pc of containers)
                container.append(pc);
        }
        var sortProducts=(cmp=ascCmp)=>
        {
            productContainers.sort(cmp);
            resetContainer(productContainers);
        }
        document.querySelector("#ascSort").addEventListener("click",()=>{sortProducts();})
        document.querySelector("#descSort").addEventListener("click",()=>{sortProducts(descCmp);})
    }
)