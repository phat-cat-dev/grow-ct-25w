## PAge progree and Home Button alignment

Square border around each - colored as tih the inner symbols and page_level indicator ) (alll their classes are accessible via )/home/abbottdev/workspace-26u/wkspc2614-adapt3/undlaf-intro_261012-235924/adapt-less-compiles you may need to trace back through the layers ri the original /home/abbottdev/workspace-26u/wkspc2614-adapt3/undlaf-intro_261012-235924/adapt-less-compiles/adapt-core-vanilla-interface.less
/home/abbottdev/workspace-26u/wkspc2614-adapt3/undlaf-intro_261012-235924/adapt-less-compiles/adapt-core-vanilla-interface-uuid.tokens.less which were the sources of the pure adpat output (its core plus its vanillas specificity) and then see /home/abbottdev/workspace-26u/wkspc2614-adapt3/undlaf-intro_261012-235924/adapt-less-compiles/ab-token-structure.less for our --ab-- base tokens whihc then point to their defaults settings which will be a combo of default --ab- settings in level 4 and them settings in levels 5 ~> ^ where ver they exits -- we firtsneed to compile a list that gievs us the final set of decideing rules for the page_level_styling settings (all of them) we cna then eihter add border in their or geenrate a new nave-icon-surround iinto the page structure with the settings for the shared sqyaure border and build our own nav component or eoverlay via the extensions






2. build me a css / less document that shows me the original
 adapt page structure classess that still get built into the page nav article block component (empty eg just teh holder) structure and can you also create script for reviewing ehich ever version of the structure tokens exist int a compiled bui;lt lessoncss and thnen create teo sheets form them - 1. that maps it through the css compilation layers tokenistically followign this pattern and create csv that layers each correspondence throught the foloowing sequence from  > col1 = raw adapt- structure-class-names/tokens (less) held in its page templates that are inserted at compile time at course nav page article block component ? component templpate (eg the ones the conpments themselves are required ot hook into) >>> Then individual named components get there own section at the end in grooups  simmilar shoudl go in ther e still and which we reach through token system its page templated > col2 the --ad-* variable we assigned to the core page stuff and nay that are in componenst > col3 the token uuid we /home/abbottdev/workspace-26u/wkspc2614-adapt3/undlaf-intro_261012-235924/adapt-less-compiles/adapt-core-vanilla-interface-uuid.tokens.less > cold 4 th etokken id we gave /home/abbottdev/workspace-26u/wkspc2614-adapt3/undlaf-intro_261012-235924/adapt-less-compiles/adapt-abbott-interface-uuid.token.less > cols 5 the token we gave in /home/abbottdev/workspace-26u/wkspc2614-adapt3/undlaf-intro_261012-235924/adapt-less-compiles/ab-token-base.less >> col 6 the prpoertis defined aginst those tokens in /home/abbottdev/workspace-26u/wkspc2614-adapt3/undlaf-intro_261012-235924/adapt-less-compiles/ab-token-values.less > then col6 /home/abbottdev/workspace-26u/wkspc2614-adapt3/undlaf-intro_261012-235924/adapt-less-compiles/ab-token-base.less > then a column that tells me the defaukts in LAyer 4 (--ab-base defaults)  OR are being OVERWRITTEN by the them token in the next cllumns >> next col the thematinc templatetoken doing the overwrtiign >> then next column the actual Layer 6 theme stting -- SO basically a csv of all the LEASS/ccss processes including all the tookens and (where the values in the comments are useful include tehn as sadditional column  inbetween the payers if needs e )Basiclaly a big refernce  csv I cna covert to .xml / json templates and manufacture a viewer toi see my adapt > ab > user them process and from that genertat blocks of themable sections and give them to end user in an answer sheet settings form they can fill in and I can use to generate a nw theme soi we ar ebuilding the data flows (we actually bypass the uuid equalling eg --ad-uusid- to --ab-uuid-  becasue once we mapped named tokens across it was wasted and so we have adap-out (core + valnilla) to abbott-semnatic tokens btu I wabnt to include the uuid data for posterity and incase it becomes relavnt to use i nfuture )
  and fileter and then we build 


<span class="pagelevelprogress__indicator-outer is-menu-item is-incomplete" style="--adapt-pagelevelprogress-percentage: 0%;"><span class="pagelevelprogress__indicator"><span class="pagelevelprogress__indicator-inner"><span class="pagelevelprogress__indicator-bar"></span><span class="aria-label">Page completion 0%</span></span></span></span>

and

<button class="btn-icon nav__btn nav__back-btn js-nav-back-btn" aria-label="Back" data-tooltip-id="back" role="link" aria-describedby="tooltip-back" name="backButton" data-order="0" data-event="backButton">
    <span class="icon" aria-hidden="true"></span>
    <span class="nav__btn-label" aria-hidden="true">Back</span>
  </button>


ww may not want the page level indicator appearign without tthe surround that it will hav ein the navba when it is fo rexample in the menu tiles or on pages... or maybe w will - it would be good to have them stand out where they appear with a lebl Eg: Activity progress or Sections progress - and then the trickle turns thme ot ocmplete the title switches to ocmplete (is their a mcahanism fo rthis?>

Bcaiscally we ned to invetsigate the page level
#



## css refix

Map Layer 3 - and review the programtttic against teh structured - and we getit set to a core organisation of commonly used areas eg those common structures and anyway we rveiew Layer 3 struturally and organisationally and we come up with a default 'view' of it (a json template that mearri) that we prefer at layer 3 to view / export. (with layers named and commented - relationships to other sections mapped - basically a bit of metadataa for the sections  - from that we genrerate a 'view' frrameowk to the raw css delcarations that exits in layer 4 and 'view layer 4 as layer 3 but structurally and as css / less delarsaation )


  

    

