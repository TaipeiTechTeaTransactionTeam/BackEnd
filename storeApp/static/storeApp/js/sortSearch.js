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
        function asc(a,b)
        {
            if(getPrice(a)<getPrice(b))
                return 1;
            else if(getPrice(a)>getPrice(b))
                return -1;
            return 0;
        }
        function desc(a,b)
        {
            return asc(b,a)
        }
        function resetContainer(containers)
        {
            container.innerHTML="";
            for(var pc of containers)
                container.append(pc);
        }
        productContainers.sort(desc);
        resetContainer(productContainers);
        
    }
)