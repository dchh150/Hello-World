from xml.dom.minidom import parse
import xml.dom.minidom


def printdata(futree,tagname):
    tname = futree.getElementsByTagName(tagname)
    try:
        return tname[0].childNodes[0].data
    except:
        return ""


def printAddionLing(fileN):
    #查找有聚灵作用的物品
    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse(fileN)
    ThingDefs = DOMTree.documentElement
    ThingDef = ThingDefs.getElementsByTagName("ThingDef")
    if not ThingDef:
        return None
    for thing in ThingDef:
        #nextif = printdata(thing,"AddionLing") and printdata(thing,"AddionRadius") and float(printdata(thing,"AddionLing")) > 0 and float(printdata(thing,"AddionRadius")) > 0
        nextif = printdata(thing,"AddionLing") and float(printdata(thing,"AddionLing")) > 0 
        if nextif:
            print(printdata(thing,"ThingName"), end =";")
            print(printdata(thing,"AddionLing"), end =";")
            print(printdata(thing,"AddionRadius"), end =";")
            print(printdata(thing,"AddionFailing"), end =";")
            print(printdata(thing,"AddionFailRadius"), end =";")
            Element = thing.getElementsByTagName("Element")
            if Element:
                print(printdata(Element[0],"Kind"), end =";")
                print(printdata(Element[0],"Value"), end =";")
                print(printdata(Element[0],"Radius"), end =";")
            print('')


def printAccommodate(fileN):
    #查找物品吸收灵力效率
    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse(fileN)
    ThingDefs = DOMTree.documentElement
    ThingDef = ThingDefs.getElementsByTagName("ThingDef")
    somest = ["ThingName","Attenuation","Absorption","Accommodate"]
    def nextif(et):
        return printdata(et,"Accommodate") and float(printdata(et,"Accommodate")) > 1
    if not ThingDef:
        return None
    for st in somest:
        print(st, end =";")
    print('')
    for thing in ThingDef:
        if not nextif(thing):
            continue
        for st in somest:
            print(printdata(thing,st), end =";")    
        print('')

if __name__ == "__main__":
    docs=[
        r"D:\MyDocuments\Desktop\Settings\TerrainDef\Terrain_Base.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Building\Building_Magic.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Building\Building_Ornament2.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Building\Building_Production.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Boss.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Consumable_Dan.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Consumable_Drug.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Equipment_MiBao.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_FengShuiItem.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_2_MetalBlock.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_2_RockBlock.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_2_WoodBlock.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_Metal.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_Rock.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_Wood.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_System.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Plant\Plant_LingZhi.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Plant\Plant_Tree.xml"
    ]
    for doc in docs:
        try:
            printAddionLing(doc)
            #printAccommodate(doc)
        except:
            print("查询失败的文件：",doc)
    input("按任意键退出")