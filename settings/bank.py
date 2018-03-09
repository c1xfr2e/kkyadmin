#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'zh'
__date__ = '4/22/15'


BANKS = [
   {"name": "中国工商银行", "id": 10000},
   {"name": "中国农业银行", "id": 10001},
   {"name": "中国银行", "id": 10002},
   {"name": "中国建设银行", "id": 10003},
   {"name": "交通银行", "id": 10005},
   {"name": "招商银行", "id": 10006}
]


CITIES = [
    {"cityId":10001,"province":"北京市","name":"北京市"},
    {"cityId":10002,"province":"天津市","name":"天津市"},
    {"cityId":10003,"province":"河北省","name":"石家庄市"},
    {"cityId":10004,"province":"河北省","name":"唐山市"},
    {"cityId":10005,"province":"河北省","name":"秦皇岛市"},
    {"cityId":10006,"province":"河北省","name":"邯郸市"},
    {"cityId":10007,"province":"河北省","name":"邢台市"},
    {"cityId":10008,"province":"河北省","name":"保定市"},
    {"cityId":10009,"province":"河北省","name":"张家口市"},
    {"cityId":10010,"province":"河北省","name":"承德市"},
    {"cityId":10011,"province":"河北省","name":"沧州市"},
    {"cityId":10012,"province":"河北省","name":"廊坊市"},
    {"cityId":10013,"province":"河北省","name":"衡水市"},
    {"cityId":10014,"province":"山西省","name":"太原市"},
    {"cityId":10015,"province":"山西省","name":"大同市"},
    {"cityId":10016,"province":"山西省","name":"阳泉市"},
    {"cityId":10017,"province":"山西省","name":"长治市"},
    {"cityId":10018,"province":"山西省","name":"晋城市"},
    {"cityId":10019,"province":"山西省","name":"朔州市"},
    {"cityId":10020,"province":"山西省","name":"晋中市"},
    {"cityId":10021,"province":"山西省","name":"运城市"},
    {"cityId":10022,"province":"山西省","name":"忻州市"},
    {"cityId":10023,"province":"山西省","name":"临汾市"},
    {"cityId":10024,"province":"山西省","name":"吕梁市"},
    {"cityId":10025,"province":"内蒙古","name":"呼和浩特市"},
    {"cityId":10026,"province":"内蒙古","name":"包头市"},
    {"cityId":10027,"province":"内蒙古","name":"乌海市"},
    {"cityId":10028,"province":"内蒙古","name":"赤峰市"},
    {"cityId":10029,"province":"内蒙古","name":"通辽市"},
    {"cityId":10030,"province":"内蒙古","name":"鄂尔多斯市"},
    {"cityId":10031,"province":"内蒙古","name":"呼伦贝尔市"},
    {"cityId":10032,"province":"内蒙古","name":"巴彦淖尔市"},
    {"cityId":10033,"province":"内蒙古","name":"乌兰察布市"},
    {"cityId":10034,"province":"内蒙古","name":"兴安盟"},
    {"cityId":10035,"province":"内蒙古","name":"锡林郭勒盟"},
    {"cityId":10036,"province":"内蒙古","name":"阿拉善盟"},
    {"cityId":10037,"province":"辽宁省","name":"沈阳市"},
    {"cityId":10038,"province":"辽宁省","name":"大连市"},
    {"cityId":10039,"province":"辽宁省","name":"鞍山市"},
    {"cityId":10040,"province":"辽宁省","name":"抚顺市"},
    {"cityId":10041,"province":"辽宁省","name":"本溪市"},
    {"cityId":10042,"province":"辽宁省","name":"丹东市"},
    {"cityId":10043,"province":"辽宁省","name":"锦州市"},
    {"cityId":10044,"province":"辽宁省","name":"营口市"},
    {"cityId":10045,"province":"辽宁省","name":"阜新市"},
    {"cityId":10046,"province":"辽宁省","name":"辽阳市"},
    {"cityId":10047,"province":"辽宁省","name":"盘锦市"},
    {"cityId":10048,"province":"辽宁省","name":"铁岭市"},
    {"cityId":10049,"province":"辽宁省","name":"朝阳市"},
    {"cityId":10050,"province":"辽宁省","name":"葫芦岛市"},
    {"cityId":10051,"province":"吉林省","name":"长春市"},
    {"cityId":10052,"province":"吉林省","name":"吉林市"},
    {"cityId":10053,"province":"吉林省","name":"四平市"},
    {"cityId":10054,"province":"吉林省","name":"辽源市"},
    {"cityId":10055,"province":"吉林省","name":"通化市"},
    {"cityId":10056,"province":"吉林省","name":"白山市"},
    {"cityId":10057,"province":"吉林省","name":"松原市"},
    {"cityId":10058,"province":"吉林省","name":"白城市"},
    {"cityId":10059,"province":"吉林省","name":"延边朝鲜族自治州"},
    {"cityId":10060,"province":"黑龙江省","name":"哈尔滨市"},
    {"cityId":10061,"province":"黑龙江省","name":"齐齐哈尔市"},
    {"cityId":10062,"province":"黑龙江省","name":"鸡西市"},
    {"cityId":10063,"province":"黑龙江省","name":"鹤岗市"},
    {"cityId":10064,"province":"黑龙江省","name":"双鸭山市"},
    {"cityId":10065,"province":"黑龙江省","name":"大庆市"},
    {"cityId":10066,"province":"黑龙江省","name":"伊春市"},
    {"cityId":10067,"province":"黑龙江省","name":"七台河市"},
    {"cityId":10068,"province":"黑龙江省","name":"牡丹江市"},
    {"cityId":10069,"province":"黑龙江省","name":"黑河市"},
    {"cityId":10070,"province":"黑龙江省","name":"绥化市"},
    {"cityId":10071,"province":"黑龙江省","name":"大兴安岭地区"},
    {"cityId":10072,"province":"黑龙江省","name":"佳木斯市"},
    {"cityId":10073,"province":"上海市","name":"上海市"},
    {"cityId":10074,"province":"江苏省","name":"南京市"},
    {"cityId":10075,"province":"江苏省","name":"无锡市"},
    {"cityId":10076,"province":"江苏省","name":"徐州市"},
    {"cityId":10077,"province":"江苏省","name":"常州市"},
    {"cityId":10078,"province":"江苏省","name":"苏州市"},
    {"cityId":10079,"province":"江苏省","name":"南通市"},
    {"cityId":10080,"province":"江苏省","name":"连云港市"},
    {"cityId":10081,"province":"江苏省","name":"淮安市"},
    {"cityId":10082,"province":"江苏省","name":"盐城市"},
    {"cityId":10083,"province":"江苏省","name":"扬州市"},
    {"cityId":10084,"province":"江苏省","name":"镇江市"},
    {"cityId":10085,"province":"江苏省","name":"泰州市"},
    {"cityId":10086,"province":"江苏省","name":"宿迁市"},
    {"cityId":10087,"province":"浙江省","name":"杭州市"},
    {"cityId":10088,"province":"浙江省","name":"宁波市"},
    {"cityId":10089,"province":"浙江省","name":"温州市"},
    {"cityId":10090,"province":"浙江省","name":"嘉兴市"},
    {"cityId":10091,"province":"浙江省","name":"湖州市"},
    {"cityId":10092,"province":"浙江省","name":"绍兴市"},
    {"cityId":10093,"province":"浙江省","name":"金华市"},
    {"cityId":10094,"province":"浙江省","name":"衢州市"},
    {"cityId":10095,"province":"浙江省","name":"舟山市"},
    {"cityId":10096,"province":"浙江省","name":"台州市"},
    {"cityId":10097,"province":"浙江省","name":"丽水市"},
    {"cityId":10098,"province":"安徽省","name":"合肥市"},
    {"cityId":10099,"province":"安徽省","name":"芜湖市"},
    {"cityId":10100,"province":"安徽省","name":"蚌埠市"},
    {"cityId":10101,"province":"安徽省","name":"淮南市"},
    {"cityId":10102,"province":"安徽省","name":"马鞍山市"},
    {"cityId":10103,"province":"安徽省","name":"淮北市"},
    {"cityId":10104,"province":"安徽省","name":"铜陵市"},
    {"cityId":10105,"province":"安徽省","name":"安庆市"},
    {"cityId":10106,"province":"安徽省","name":"黄山市"},
    {"cityId":10107,"province":"安徽省","name":"滁州市"},
    {"cityId":10108,"province":"安徽省","name":"阜阳市"},
    {"cityId":10109,"province":"安徽省","name":"宿州市"},
    {"cityId":10110,"province":"安徽省","name":"巢湖市"},
    {"cityId":10111,"province":"安徽省","name":"六安市"},
    {"cityId":10112,"province":"安徽省","name":"亳州市"},
    {"cityId":10113,"province":"安徽省","name":"池州市"},
    {"cityId":10114,"province":"安徽省","name":"宣城市"},
    {"cityId":10115,"province":"福建省","name":"福州市"},
    {"cityId":10116,"province":"福建省","name":"厦门市"},
    {"cityId":10117,"province":"福建省","name":"莆田市"},
    {"cityId":10118,"province":"福建省","name":"三明市"},
    {"cityId":10119,"province":"福建省","name":"泉州市"},
    {"cityId":10120,"province":"福建省","name":"漳州市"},
    {"cityId":10121,"province":"福建省","name":"南平市"},
    {"cityId":10122,"province":"福建省","name":"龙岩市"},
    {"cityId":10123,"province":"福建省","name":"宁德市"},
    {"cityId":10124,"province":"江西省","name":"南昌市"},
    {"cityId":10125,"province":"江西省","name":"景德镇市"},
    {"cityId":10126,"province":"江西省","name":"萍乡市"},
    {"cityId":10127,"province":"江西省","name":"九江市"},
    {"cityId":10128,"province":"江西省","name":"新余市"},
    {"cityId":10129,"province":"江西省","name":"鹰潭市"},
    {"cityId":10130,"province":"江西省","name":"赣州市"},
    {"cityId":10131,"province":"江西省","name":"吉安市"},
    {"cityId":10132,"province":"江西省","name":"宜春市"},
    {"cityId":10133,"province":"江西省","name":"抚州市"},
    {"cityId":10134,"province":"江西省","name":"上饶市"},
    {"cityId":10135,"province":"山东省","name":"济南市"},
    {"cityId":10136,"province":"山东省","name":"青岛市"},
    {"cityId":10137,"province":"山东省","name":"淄博市"},
    {"cityId":10138,"province":"山东省","name":"枣庄市"},
    {"cityId":10139,"province":"山东省","name":"东营市"},
    {"cityId":10140,"province":"山东省","name":"烟台市"},
    {"cityId":10141,"province":"山东省","name":"潍坊市"},
    {"cityId":10142,"province":"山东省","name":"济宁市"},
    {"cityId":10143,"province":"山东省","name":"泰安市"},
    {"cityId":10144,"province":"山东省","name":"威海市"},
    {"cityId":10145,"province":"山东省","name":"日照市"},
    {"cityId":10146,"province":"山东省","name":"莱芜市"},
    {"cityId":10147,"province":"山东省","name":"临沂市"},
    {"cityId":10148,"province":"山东省","name":"德州市"},
    {"cityId":10149,"province":"山东省","name":"聊城市"},
    {"cityId":10150,"province":"山东省","name":"滨州市"},
    {"cityId":10151,"province":"山东省","name":"菏泽市"},
    {"cityId":10152,"province":"河南省","name":"郑州市"},
    {"cityId":10153,"province":"河南省","name":"开封市"},
    {"cityId":10154,"province":"河南省","name":"洛阳市"},
    {"cityId":10155,"province":"河南省","name":"平顶山市"},
    {"cityId":10156,"province":"河南省","name":"安阳市"},
    {"cityId":10157,"province":"河南省","name":"鹤壁市"},
    {"cityId":10158,"province":"河南省","name":"新乡市"},
    {"cityId":10159,"province":"河南省","name":"焦作市"},
    {"cityId":10160,"province":"河南省","name":"濮阳市"},
    {"cityId":10161,"province":"河南省","name":"许昌市"},
    {"cityId":10162,"province":"河南省","name":"漯河市"},
    {"cityId":10163,"province":"河南省","name":"三门峡市"},
    {"cityId":10164,"province":"河南省","name":"南阳市"},
    {"cityId":10165,"province":"河南省","name":"商丘市"},
    {"cityId":10166,"province":"河南省","name":"信阳市"},
    {"cityId":10167,"province":"河南省","name":"周口市"},
    {"cityId":10168,"province":"河南省","name":"驻马店市"},
    {"cityId":10362,"province":"河南省","name":"济源市"},
    {"cityId":10169,"province":"湖北省","name":"武汉市"},
    {"cityId":10170,"province":"湖北省","name":"黄石市"},
    {"cityId":10171,"province":"湖北省","name":"十堰市"},
    {"cityId":10172,"province":"湖北省","name":"宜昌市"},
    {"cityId":10173,"province":"湖北省","name":"襄樊市"},
    {"cityId":10174,"province":"湖北省","name":"鄂州市"},
    {"cityId":10175,"province":"湖北省","name":"荆门市"},
    {"cityId":10176,"province":"湖北省","name":"孝感市"},
    {"cityId":10177,"province":"湖北省","name":"荆州市"},
    {"cityId":10178,"province":"湖北省","name":"黄冈市"},
    {"cityId":10179,"province":"湖北省","name":"咸宁市"},
    {"cityId":10180,"province":"湖北省","name":"随州市"},
    {"cityId":10181,"province":"湖北省","name":"恩施土家族苗族自治州"},
    {"cityId":10182,"province":"湖北省","name":"省直辖行政单位"},
    {"cityId":10183,"province":"湖南省","name":"长沙市"},
    {"cityId":10184,"province":"湖南省","name":"株洲市"},
    {"cityId":10185,"province":"湖南省","name":"湘潭市"},
    {"cityId":10186,"province":"湖南省","name":"衡阳市"},
    {"cityId":10187,"province":"湖南省","name":"邵阳市"},
    {"cityId":10188,"province":"湖南省","name":"岳阳市"},
    {"cityId":10189,"province":"湖南省","name":"常德市"},
    {"cityId":10190,"province":"湖南省","name":"张家界市"},
    {"cityId":10191,"province":"湖南省","name":"益阳市"},
    {"cityId":10192,"province":"湖南省","name":"郴州市"},
    {"cityId":10193,"province":"湖南省","name":"永州市"},
    {"cityId":10194,"province":"湖南省","name":"怀化市"},
    {"cityId":10195,"province":"湖南省","name":"娄底市"},
    {"cityId":10196,"province":"湖南省","name":"湘西土家族苗族自治州"},
    {"cityId":10197,"province":"广东省","name":"广州市"},
    {"cityId":10198,"province":"广东省","name":"韶关市"},
    {"cityId":10199,"province":"广东省","name":"深圳市"},
    {"cityId":10200,"province":"广东省","name":"珠海市"},
    {"cityId":10201,"province":"广东省","name":"汕头市"},
    {"cityId":10202,"province":"广东省","name":"佛山市"},
    {"cityId":10203,"province":"广东省","name":"江门市"},
    {"cityId":10204,"province":"广东省","name":"湛江市"},
    {"cityId":10205,"province":"广东省","name":"茂名市"},
    {"cityId":10206,"province":"广东省","name":"肇庆市"},
    {"cityId":10207,"province":"广东省","name":"惠州市"},
    {"cityId":10208,"province":"广东省","name":"梅州市"},
    {"cityId":10209,"province":"广东省","name":"汕尾市"},
    {"cityId":10210,"province":"广东省","name":"河源市"},
    {"cityId":10211,"province":"广东省","name":"阳江市"},
    {"cityId":10212,"province":"广东省","name":"清远市"},
    {"cityId":10213,"province":"广东省","name":"东莞市"},
    {"cityId":10214,"province":"广东省","name":"中山市"},
    {"cityId":10215,"province":"广东省","name":"潮州市"},
    {"cityId":10216,"province":"广东省","name":"揭阳市"},
    {"cityId":10217,"province":"广东省","name":"云浮市"},
    {"cityId":10218,"province":"广西","name":"南宁市"},
    {"cityId":10219,"province":"广西","name":"柳州市"},
    {"cityId":10220,"province":"广西","name":"桂林市"},
    {"cityId":10221,"province":"广西","name":"梧州市"},
    {"cityId":10222,"province":"广西","name":"北海市"},
    {"cityId":10223,"province":"广西","name":"防城港市"},
    {"cityId":10224,"province":"广西","name":"钦州市"},
    {"cityId":10225,"province":"广西","name":"贵港市"},
    {"cityId":10226,"province":"广西","name":"玉林市"},
    {"cityId":10227,"province":"广西","name":"百色市"},
    {"cityId":10228,"province":"广西","name":"贺州市"},
    {"cityId":10229,"province":"广西","name":"河池市"},
    {"cityId":10230,"province":"广西","name":"来宾市"},
    {"cityId":10231,"province":"广西","name":"崇左市"},
    {"cityId":10232,"province":"海南省","name":"海口市"},
    {"cityId":10233,"province":"海南省","name":"三亚市"},
    {"cityId":10234,"province":"重庆市","name":"重庆市"},
    {"cityId":10235,"province":"四川省","name":"成都市"},
    {"cityId":10236,"province":"四川省","name":"自贡市"},
    {"cityId":10237,"province":"四川省","name":"攀枝花市"},
    {"cityId":10238,"province":"四川省","name":"泸州市"},
    {"cityId":10239,"province":"四川省","name":"德阳市"},
    {"cityId":10240,"province":"四川省","name":"绵阳市"},
    {"cityId":10241,"province":"四川省","name":"广元市"},
    {"cityId":10242,"province":"四川省","name":"遂宁市"},
    {"cityId":10243,"province":"四川省","name":"内江市"},
    {"cityId":10244,"province":"四川省","name":"乐山市"},
    {"cityId":10245,"province":"四川省","name":"南充市"},
    {"cityId":10246,"province":"四川省","name":"眉山市"},
    {"cityId":10247,"province":"四川省","name":"宜宾市"},
    {"cityId":10248,"province":"四川省","name":"广安市"},
    {"cityId":10249,"province":"四川省","name":"达州市"},
    {"cityId":10250,"province":"四川省","name":"雅安市"},
    {"cityId":10251,"province":"四川省","name":"巴中市"},
    {"cityId":10252,"province":"四川省","name":"资阳市"},
    {"cityId":10253,"province":"四川省","name":"阿坝藏族羌族自治州"},
    {"cityId":10254,"province":"四川省","name":"甘孜藏族自治州"},
    {"cityId":10255,"province":"四川省","name":"凉山彝族自治州"},
    {"cityId":10256,"province":"贵州省","name":"贵阳市"},
    {"cityId":10257,"province":"贵州省","name":"六盘水市"},
    {"cityId":10258,"province":"贵州省","name":"遵义市"},
    {"cityId":10259,"province":"贵州省","name":"安顺市"},
    {"cityId":10260,"province":"贵州省","name":"铜仁地区"},
    {"cityId":10261,"province":"贵州省","name":"黔西南布依族苗族自治州"},
    {"cityId":10262,"province":"贵州省","name":"毕节地区"},
    {"cityId":10263,"province":"贵州省","name":"黔东南苗族侗族自治州"},
    {"cityId":10264,"province":"贵州省","name":"黔南布依族苗族自治州"},
    {"cityId":10265,"province":"云南省","name":"昆明市"},
    {"cityId":10266,"province":"云南省","name":"曲靖市"},
    {"cityId":10267,"province":"云南省","name":"玉溪市"},
    {"cityId":10268,"province":"云南省","name":"保山市"},
    {"cityId":10269,"province":"云南省","name":"昭通市"},
    {"cityId":10270,"province":"云南省","name":"丽江市"},
    {"cityId":10271,"province":"云南省","name":"思茅市"},
    {"cityId":10272,"province":"云南省","name":"临沧市"},
    {"cityId":10273,"province":"云南省","name":"楚雄彝族自治州"},
    {"cityId":10274,"province":"云南省","name":"红河哈尼族彝族自治州"},
    {"cityId":10275,"province":"云南省","name":"文山壮族苗族自治州"},
    {"cityId":10276,"province":"云南省","name":"西双版纳傣族自治州"},
    {"cityId":10277,"province":"云南省","name":"大理白族自治州"},
    {"cityId":10278,"province":"云南省","name":"德宏傣族景颇族自治州"},
    {"cityId":10279,"province":"云南省","name":"怒江傈僳族自治州"},
    {"cityId":10280,"province":"云南省","name":"迪庆藏族自治州"},
    {"cityId":10281,"province":"西藏","name":"拉萨市"},
    {"cityId":10282,"province":"西藏","name":"昌都地区"},
    {"cityId":10283,"province":"西藏","name":"山南地区"},
    {"cityId":10284,"province":"西藏","name":"日喀则地区"},
    {"cityId":10285,"province":"西藏","name":"那曲地区"},
    {"cityId":10286,"province":"西藏","name":"阿里地区"},
    {"cityId":10287,"province":"西藏","name":"林芝地区"},
    {"cityId":10288,"province":"陕西省","name":"西安市"},
    {"cityId":10289,"province":"陕西省","name":"铜川市"},
    {"cityId":10290,"province":"陕西省","name":"宝鸡市"},
    {"cityId":10291,"province":"陕西省","name":"咸阳市"},
    {"cityId":10292,"province":"陕西省","name":"渭南市"},
    {"cityId":10293,"province":"陕西省","name":"延安市"},
    {"cityId":10294,"province":"陕西省","name":"汉中市"},
    {"cityId":10295,"province":"陕西省","name":"榆林市"},
    {"cityId":10296,"province":"陕西省","name":"安康市"},
    {"cityId":10297,"province":"陕西省","name":"商洛市"},
    {"cityId":10298,"province":"甘肃省","name":"兰州市"},
    {"cityId":10299,"province":"甘肃省","name":"嘉峪关市"},
    {"cityId":10300,"province":"甘肃省","name":"金昌市"},
    {"cityId":10301,"province":"甘肃省","name":"白银市"},
    {"cityId":10302,"province":"甘肃省","name":"天水市"},
    {"cityId":10303,"province":"甘肃省","name":"武威市"},
    {"cityId":10304,"province":"甘肃省","name":"张掖市"},
    {"cityId":10305,"province":"甘肃省","name":"平凉市"},
    {"cityId":10306,"province":"甘肃省","name":"酒泉市"},
    {"cityId":10307,"province":"甘肃省","name":"庆阳市"},
    {"cityId":10308,"province":"甘肃省","name":"定西市"},
    {"cityId":10309,"province":"甘肃省","name":"陇南市"},
    {"cityId":10310,"province":"甘肃省","name":"临夏回族自治州"},
    {"cityId":10311,"province":"甘肃省","name":"甘南藏族自治州"},
    {"cityId":10312,"province":"青海省","name":"西宁市"},
    {"cityId":10313,"province":"青海省","name":"海东地区"},
    {"cityId":10314,"province":"青海省","name":"海北藏族自治州"},
    {"cityId":10315,"province":"青海省","name":"黄南藏族自治州"},
    {"cityId":10316,"province":"青海省","name":"海南藏族自治州"},
    {"cityId":10317,"province":"青海省","name":"果洛藏族自治州"},
    {"cityId":10318,"province":"青海省","name":"玉树藏族自治州"},
    {"cityId":10319,"province":"青海省","name":"海西蒙古族藏族自治州"},
    {"cityId":10320,"province":"宁夏","name":"银川市"},
    {"cityId":10321,"province":"宁夏","name":"石嘴山市"},
    {"cityId":10322,"province":"宁夏","name":"吴忠市"},
    {"cityId":10323,"province":"宁夏","name":"固原市"},
    {"cityId":10324,"province":"宁夏","name":"中卫市"},
    {"cityId":10325,"province":"新疆","name":"乌鲁木齐市"},
    {"cityId":10326,"province":"新疆","name":"克拉玛依市"},
    {"cityId":10327,"province":"新疆","name":"吐鲁番地区"},
    {"cityId":10328,"province":"新疆","name":"哈密地区"},
    {"cityId":10329,"province":"新疆","name":"昌吉回族自治州"},
    {"cityId":10330,"province":"新疆","name":"博尔塔拉蒙古自治州"},
    {"cityId":10331,"province":"新疆","name":"巴音郭楞蒙古自治州"},
    {"cityId":10332,"province":"新疆","name":"阿克苏地区"},
    {"cityId":10333,"province":"新疆","name":"克孜勒苏柯尔克孜自治州"},
    {"cityId":10334,"province":"新疆","name":"喀什地区"},
    {"cityId":10335,"province":"新疆","name":"和田地区"},
    {"cityId":10336,"province":"新疆","name":"伊犁哈萨克自治州"},
    {"cityId":10337,"province":"新疆","name":"塔城地区"},
    {"cityId":10338,"province":"新疆","name":"阿勒泰地区"},
    {"cityId":10339,"province":"新疆","name":"省直辖行政单位"}
]