{
    "name" : "Real Estate",
    "summary" : "Test Module",
    "version" : "17.0.0.0.0",
    "license" : "OEEL-1",
    "depends" : ["crm",],
    "data" : [
        #SECURITY
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        #VIEWS
        "views/estate_property_views.xml",
        "views/estate_menus.xml",
        #MENUES        
        ],
    "demo" : ["demo/demo.xml"]    
}