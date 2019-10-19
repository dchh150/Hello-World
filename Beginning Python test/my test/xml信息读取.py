from xml.dom.minidom import parse
import xml.dom.minidom


def printAddionLing(fileN):
    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse(fileN)
    ThingDefs = DOMTree.documentElement

    def printdata(futree,tagname):
        tname = futree.getElementsByTagName(tagname)
        try:
            return tname[0].childNodes[0].data
        except:
            return ""

    ThingDef = ThingDefs.getElementsByTagName("ThingDef")
    if not ThingDef:
        return None
    for thing in ThingDef:
        nextif = printdata(thing,"AddionLing") and printdata(thing,"AddionRadius") and float(printdata(thing,"AddionLing")) > 0 and float(printdata(thing,"AddionRadius")) > 0
        if nextif:
            print(printdata(thing,"ThingName"), end ="\t")
            print(printdata(thing,"AddionLing"), end ="\t")
            print(printdata(thing,"AddionRadius"), end ="\t")
            print(printdata(thing,"AddionFailing"), end ="\t")
            print(printdata(thing,"AddionFailRadius"), end ="\t")
            Element = thing.getElementsByTagName("Element")
            if Element:
                print(printdata(Element[0],"Kind"), end ="\t")
                print(printdata(Element[0],"Value"), end ="\t")
                print(printdata(Element[0],"Radius"), end ="\t")
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
        except:
            print(doc)
    input("按任意键退出")