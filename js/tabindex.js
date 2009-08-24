function Show_TabsMenu(tabadid_num,tabadnum){
	for(var i=0;i<16;i++){document.getElementById("tabadcontent_"+tabadid_num+i).style.display="none";}
	for(var i=0;i<16;i++){document.getElementById("tabadmenu_"+tabadid_num+i).className="";}
	document.getElementById("tabadmenu_"+tabadid_num+tabadnum).className="selected";
	document.getElementById("tabadcontent_"+tabadid_num+tabadnum).style.display="block";
}

function Show_ssTabsMenu(sstabadid_num,sstabadnum){
	for(var a=0;a<4;a++){document.getElementById("sstabadcontent_"+sstabadid_num+a).style.display="none";}
	for(var a=0;a<4;a++){document.getElementById("sstabadmenu_"+sstabadid_num+a).className="";}
	document.getElementById("sstabadmenu_"+sstabadid_num+sstabadnum).className="TabsClick";
	document.getElementById("sstabadcontent_"+sstabadid_num+sstabadnum).style.display="block";
}

function Show_cdTabsMenu(cdtabadid_num,cdtabadnum){
	for(var a=0;a<3;a++){document.getElementById("cdtabadcontent_"+cdtabadid_num+a).style.display="none";}
	for(var a=0;a<3;a++){document.getElementById("cdtabadmenu_"+cdtabadid_num+a).className="";}
	document.getElementById("cdtabadmenu_"+cdtabadid_num+cdtabadnum).className="TabsClick";
	document.getElementById("cdtabadcontent_"+cdtabadid_num+cdtabadnum).style.display="block";
}

function Show_smTabsMenu(smtabadid_num,smtabadnum){
	for(var a=0;a<4;a++){document.getElementById("smtabadcontent_"+smtabadid_num+a).style.display="none";}
	for(var a=0;a<4;a++){document.getElementById("smtabadmenu_"+smtabadid_num+a).className="";}
	document.getElementById("smtabadmenu_"+smtabadid_num+smtabadnum).className="TabsClick";
	document.getElementById("smtabadcontent_"+smtabadid_num+smtabadnum).style.display="block";
}

function Show_fzTabsMenu(fztabadid_num,fztabadnum){
	for(var a=0;a<3;a++){document.getElementById("fztabadcontent_"+fztabadid_num+a).style.display="none";}
	for(var a=0;a<3;a++){document.getElementById("fztabadmenu_"+fztabadid_num+a).className="";}
	document.getElementById("fztabadmenu_"+fztabadid_num+fztabadnum).className="TabsClick";
	document.getElementById("fztabadcontent_"+fztabadid_num+fztabadnum).style.display="block";
}