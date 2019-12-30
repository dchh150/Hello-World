from xml.dom.minidom import parse
import xml.dom.minidom


def printdata(futree,tagname):
    try:
        tname = futree.getElementsByTagName(tagname)
        return tname[0].childNodes[0].data
    except:
        return ""


def SubFindData(futree,subtreelist,datalist):
    try:
        if not futree:
            return None
        temptree = futree
        for subtree in subtreelist:
            if temptree.getElementsByTagName(subtree):
                temptree = temptree.getElementsByTagName(subtree)
            else:
                for data in datalist:
                    print("",end=";")
                return None
        for data in datalist:
            print(printdata(temptree[0],data), end =";")
        return True
    except:
        print("SubFindData() 函数错误")



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
            SubFindData(thing,["Element"],["Kind","Value","Radius"])
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


def printHeat(fileN):
    #查找物品温度信息
    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse(fileN)
    ThingDefs = DOMTree.documentElement
    ThingDef = ThingDefs.getElementsByTagName("ThingDef")
    somest = ["ThingName"]
    Heatst = ['Value','Radius','RoomValue','Failing','FailRadius']
    Elementst = ['Kind','Value']
    def nextif(et):
        return printdata(et,"Heat")

    for st in somest:
        print(st, end =";")
    for st in Heatst: print(st, end =";")
    for st in Elementst: print(st, end =";")
    print('')

    for thing in ThingDef:
        if not nextif(thing):
            continue
        for st in somest:
            print(printdata(thing,st), end =";")
            SubFindData(thing,["Heat"],Heatst)
            SubFindData(thing,["Element"],Elementst)
        print('')

    return True



if __name__ == "__main__":
    docs=[
        r"D:\MyDocuments\Desktop\Settings\MapStories\MapStory_FillingLv1.xml",
        r"D:\MyDocuments\Desktop\Settings\MapStories\MapStory_Item.xml",
        r"D:\MyDocuments\Desktop\Settings\MapStories\MapStory_Special.xml",
        r"D:\MyDocuments\Desktop\Settings\Npc\Race\Race_Animal.xml",
        r"D:\MyDocuments\Desktop\Settings\Npc\Race\Race_Boss.xml",
        r"D:\MyDocuments\Desktop\Settings\Npc\Race\Race_BossTest.xml",
        r"D:\MyDocuments\Desktop\Settings\Npc\Race\Race_JYAnimal.xml",
        r"D:\MyDocuments\Desktop\Settings\Npc\SpDrop\SpDrop_DaNeng.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Building\Building_Base.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Building\Building_Floor.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Building\Building_Furniture.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Building\Building_Magic.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Building\Building_Ornament.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Building\Building_Ornament2.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Building\Building_Other.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Building\Building_Production.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Building\Building_Roof.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Building\Building_System.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Building\Building_Wall.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Base.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Boss.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Consumable_Dan.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Consumable_Drug.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Consumable_Food.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Consumable_SoulCrystal.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Consumable_Spell.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Consumable_Tool.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Equipment_Clothes.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Equipment_Fabao.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Equipment_Hat.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Equipment_MiBao.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Equipment_Trousers.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Equipment_Weapon.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_FengShuiItem.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_2_Ingredient.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_2_LeftoverMaterial.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_2_Meat.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_2_MetalBlock.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_2_RockBlock.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_2_WoodBlock.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_Bone.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_Cloth.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_Leather.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_Metal.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_Other.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_Plant.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_PlantProduct.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_Rock.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_Material_Wood.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\Item_System.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Item\RaceNormalAttack.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Plant\Plant_Base.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Plant\Plant_Beauty.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Plant\Plant_Box.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Plant\Plant_Farm.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Plant\Plant_LingZhi.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Plant\Plant_Special.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Plant\Plant_Tree.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Plant\Plant_Wild.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Rock\Metal.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Rock\Rock.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Rock\RockBase.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\Rock\Special.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\ThingNpc.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\ThingSpace.xml",
        r"D:\MyDocuments\Desktop\Settings\ThingDef\ThingSystem.xml",
        r"D:\MyDocuments\Desktop\Settings\World\Places\Level1.xml",
        r"D:\MyDocuments\Desktop\Settings\World\Places\Level2.xml",
        r"D:\MyDocuments\Desktop\Settings\World\Places\Level3.xml"
    ]
    
    for doc in docs:
        try:
            #printAddionLing(doc)
            #printAccommodate(doc)
            printHeat(doc)
        except:
            print("查询失败的文件：",doc)
    input("按任意键退出")