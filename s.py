# -*- coding:utf-8 -*-
from negiXa import *
import json, time, random, tempfile, os, sys, urllib.request, urllib.parse, urllib.error, threading, codecs, datetime
import imp
imp.reload(sys)

try:
    f = open('client.csv','r')
    token = f.read()
    client=LineClient(authToken=token)
    f.close()
except:
    client = LineClient()
    f = open('client.csv','w')
    f.write(client.authToken)
    f.close()
    
poll = LinePoll(client)
#channel = LineChannel(client)
profile = client.getProfile()

helps ="""≪基本機能に関するhelpです。≫

☞ヘルプ…このhelpを表示します。
☞設定:ヘルプ…保護機能や自動参加等の各種機能に関するhelpを表示します。
☞ブラリス:ヘルプ…ブラリスに関するヘルプを表示します。
☞速度…半botの処理速度を送信します。
☞mid…midを表示します。
☞mid確認 @…メンションしたユーザーのmidを表示します。
☞gid…gid(GroupId)を表示します。
☞招待: …midを使用し招待を行います。
☞Me…自分の連絡先を表示します。
☞追加URL…自分の追加URLを送信します。
☞連絡先表示: …midから連絡先を作成します。
☞招待URL許可…招待URLをオンにします。
☞招待URL拒否…招待URLをオフにします。
☞招待URL生成…招待URLを生成します。
☞招待URL: …gidから招待URLを作成します。
☞Nk: …グループから指定した名前のユーザーを退会させます。
☞Mk @…メンションしたユーザーを退会させます。
☞停止…半botの全機能を終了します。

ねぎえる™のLINE@
http://line.me/ti/p/%40ubg0555p"""

sethelps ="""≪各種設定に関するhelpです。≫

☞全保護:オン/オフ…搭載されている全ての保護機能をオン/オフにします。
☞蹴り保護:オン/オフ…自分以外による強制退会を禁止します。
☞URL保護:オン…自分以外によるURL設定変更を禁止します。
☞招待保護:オン/オフ…自分以外による招待を禁止します。
☞グル名保護:オン/オフ…自分以外によるグループ名の変更を禁止します。
☞グル画保護:オン/オフ…自分以外によるグル画の変更を禁止します。
☞連絡先:オン/オフ…連絡先情報の表示をオン/オフにします。
☞自動追加:オン/オフ…友達の自動追加をオン/オフにします。
☞追加挨拶:オン/オフ…友達追加時の挨拶をオン/オフにします。
☞追加挨拶変更 : …友達追加時の挨拶を変更します。
☞自動参加:オン/オフ…グループ自動参加をオン/オフにします。
☞参加挨拶:オン/オフ…参加メッセージをオン/オフにします。
☞参加挨拶変更 : …グループ参加時の挨拶を変更します。
☞強制退出:オン/オフ…強制の自動退出をオン/オフにします。
☞共有:オン/オフ…ノートアルバムの情報をオン/オフにします。
☞ブラリス:オン/オフ…詳細は｢ブラリス:ヘルプ｣をご覧下さい。
☞設定確認…設定状況を確認します。

ねぎえる™のLINE@
http://line.me/ti/p/%40ubg0555p"""

bhelp="""《ブラリス機能に関するヘルプです。》

☞ブラリス:オン/オフ…ブラリス機能をオン/オフにします。
☞ブラリス追加…連絡先でブラックリストに追加します。
☞ブラリス解除…連絡先でブラックリストから削除します。
☞ブラリス追加 @…メンションでブラックリストに追加します。
☞ブラリス解除 @…メンションでブラックリストから削除します。
☞全ブラリス確認…ブラックリストユーザーを確認します。
☞ブラリス確認…グループ内にいるブラリスを確認します。
☞ブラリス排除…グループ内にいるブラリスを退会させます。
☞全ブラリス削除…全てのブラリスを解除します。

※ブラリス関連コマンド使用時にのみエラーが発生する場合、ブラリス機能がオフにされている事が原因と考えられます。ご確認ください。

ねぎえる™のLINE@
http://line.me/ti/p/%40ubg0555p"""

stop = {
	'PI' : {},  #画像保護
	'PN' : {},  #名前保護
	'PK' : {},  #蹴り保護
	'PU' : {},  #URL保護
	'PP' : {},  #招待保護
	'aam':"",
	'ajm':"",
	'contact': False,
	'aaf': False,
	'aafm': False,
	'aj': False,
	'ajfm':False,
	'arl': False,
	'noto':False,
	'db':False,
    'wb':False,
    'blc':True,
    'bls': {}
}

f=codecs.open('PP.json','r','utf-8')
stop["PP"] = json.load(f)
f=codecs.open('PN.json','r','utf-8')
stop["PN"] = json.load(f)
f=codecs.open('PI.json','r','utf-8')
stop["PI"] = json.load(f)
f=codecs.open('PK.json','r','utf-8')
stop["PK"] = json.load(f)
f=codecs.open('PU.json','r','utf-8')
stop["PU"] = json.load(f)
f=codecs.open('black.json','r','utf-8')
stop["bls"] = json.load(f)

gname = {}
gname = stop["PN"]


while True:
	try:
		ops = poll.singleTrace(count=50)
		if ops != None:
			for op in ops:
				
				if op.type == 5:
					try:
					    if stop["aaf"] == True:
					    	client.findAndAddContactsByMid(op.param1)
					    if stop["aafm"] == True:
					    	client.sendMessage(op.param1,stop["aam"])
					    if stop["aj"] == True:
					    	client.findAndAddContactsByMid(op.param1)
					    if stop["ajfm"] == True:
					    	client.sendMessage(op.param1,stop["ajm"])
					except:
						pass

				if op.type == 11:
					if op.param3 == "1":
						if op.param1 in stop['PN']:
							G = client.getGroup(op.param1)
							G.name = gname[op.param1]
							client.updateGroup(G)
							client.kickoutFromGroup(op.param1,[op.param2])
							client.sendMessage(op.param1, 'グル名保護中のグループ名変更は禁止されています。')

					if op.param3 == "2":
						if op.param1 in stop['PI']:
							client.updateGroupPicture(op.param1, op.param1 + '.png')
							client.kickoutFromGroup(op.param1,[op.param2])
							client.sendMessage(op.param1, 'グル画保護中のグループ画像変更は禁止されています。')
							
				if op.type == 11:
						if op.param1 in stop['PU']:
							G = client.getGroup(op.param1)
							G.preventedJoinByTicket = True
							client.updateGroup(G)
							client.kickoutFromGroup(op.param1,[op.param2])
							client.sendMessage(op.param1, 'URL保護中のURL変更は禁止されています。')
							
				if op.type == 19:
						if op.param1 in stop['PK']:
							G = client.getGroup(op.param1)
							client.kickoutFromGroup(op.param1,[op.param2])
							client.sendMessage(op.param1, '蹴り保護中の強制退会は禁止されています。')
					
				if op.type == 13:
					if profile.mid in op.param3:
						if stop["aj"] == True:
							client.acceptGroupInvitation(op.param1)
							client.sendMessage(op.param1,stop["ajm"])
						else:
							pass
					if op.param1 in stop["PP"]:
						Inviter = op.param3.replace("",',')
						InviterX = Inviter.split(",")
						client.cancelGroupInvitation(op.param1, InviterX)
						client.sendMessage(op.param1,"招待保護中の招待は禁止されています。")
					else:
						Inviter = op.param3.replace("",',')
						InviterX = Inviter.split(",")
						matched_list = []
						for tag in stop["bls"]:
							matched_list+=filter(lambda str: str == tag, InviterX)
						if matched_list == []:
							pass
						else:
							client.cancelGroupInvitation(op.param1, matched_list)
							client.sendMessage(op.param1,"ブラリスが招待された為ブラックリスの招待をキャンセルしました。")

				if op.type == 19:
					if stop['blc'] == True:
						if op.param2 in profile.mid:
							pass
						else:
							stop["bls"][op.param2] = True
							f=codecs.open('black.json','w','utf-8')
							json.dump(stop["bls"], f, sort_keys=True, indent=4,ensure_ascii=False)


				if op.type == 22:
					if stop["arl"] == True:
						client.leaveRoom(op.param1)

				if op.type == 25:
					msg = op.message
					try:
						if msg.contentType == 0:
							#############################################
							if msg.text in ["help","ヘルプ","へるぷ"]:
								client.sendMessage(msg.to, helps)
							#############################################
							if msg.text in ["設定:ヘルプ"]:
								client.sendMessage(msg.to, sethelps)
							#############################################
							if msg.text in ["ブラリス:ヘルプ"]:
								client.sendMessage(msg.to, bhelp)
							##############################################
							if msg.text == "mid":
								client.sendMessage(msg.to, msg._from)
							##############################################
							if "mid確認" in msg.text:
								if msg.contentMetadata is not None:
									targets = []
									key = eval(msg.contentMetadata["MENTION"])
									key["MENTIONEES"][0]["M"]
									for x in key["MENTIONEES"]:
										targets.append(x["M"])
										for mid in targets:
											txt = mid
											client.sendMessage(msg.to, txt)
							##############################################
							if msg.text == "gid":
								client.sendMessage(msg.to, msg.to)
							##############################################
							if msg.text == "Me":
							    #contact = client.getContact(mid)
							    client.sendContact(msg.to, msg._from)
							##############################################
							if "追加URL" == msg.text:
								ids = client.reissueUserTicket(0,3)
								client.sendMessage(msg.to,"http://line.me/ti/p/%s" % ids)
							##############################################
							if "招待:" in msg.text:
								key = msg.text[-33:]
								client.findAndAddContactsByMid(key)
								client.inviteIntoGroup(msg.to, [key])
								contact = client.getContact(key)
								client.sendMessage(msg.to,""+contact.displayName+"さんを招待しました。")
							##############################################
							if "連絡先表示:" in msg.text:
								key = msg.text[-33:]
								client.sendMessage(msg.to, text=None, contentMetadata={'mid': key}, contentType=13)
								contact = client.getContact(key)
								client.sendMessage(msg.to, contact.displayName+"さんの連絡先です。")
							##############################################
							if msg.text == "全保護:オン":
								client.sendMessage(msg.to, "招待保護:オン")
								client.sendMessage(msg.to, "グル名保護:オン")
								client.sendMessage(msg.to, "グル画保護:オン")
								client.sendMessage(msg.to, "URL保護:オン")
								client.sendMessage(msg.to, "蹴り保護:オン")
							##############################################
							if msg.text == "全保護:オフ":
								client.sendMessage(msg.to, "招待保護:オフ")
								client.sendMessage(msg.to, "グル名保護:オフ")
								client.sendMessage(msg.to, "グル画保護:オフ")
								client.sendMessage(msg.to, "URL保護:オフ")
								client.sendMessage(msg.to, "蹴り保護:オフ")
						    ##############################################
							if msg.text == "URL保護:オン":
								if msg.to in stop['PU']:
									client.sendMessage(msg.to, "既に保護しています。")
								else:
									client.sendMessage(msg.to, "URL保護をオンにしました。")
									stop['PU'][msg.to] = msg._from
									f=codecs.open('PU.json','w','utf-8')
									json.dump(stop["PU"], f, sort_keys=True, indent=4,ensure_ascii=False)
							##############################################
							if msg.text == "URL保護:オフ":
								if msg.to in stop['PU']:
									client.sendMessage(msg.to, "URL保護をオフにしました。")
									del stop['PU'][msg.to]
									f=codecs.open('PU.json','w','utf-8')
									json.dump(stop["PP"], f, sort_keys=True, indent=4,ensure_ascii=False)
								else:
									client.sendMessage(msg.to,"既にオフにされています。")
						    ################################################
							if msg.text == "蹴り保護:オン":
								if msg.to in stop['PK']:
									client.sendMessage(msg.to, '既に保護されています。')
								else:
									stop['PK'][msg.to] = client.getGroup(msg.to).name
									f=codecs.open('PK.json','w','utf-8')
									json.dump(stop["PK"], f, sort_keys=True, indent=4,ensure_ascii=False)
									client.sendMessage(msg.to, '蹴り保護をオンにしました。')
							##############################################
							if msg.text == "蹴り保護:オフ":
								if msg.to in stop['PK']:
									client.sendMessage(msg.to, '蹴り保護をオフにしました。')
									del stop['PK'][msg.to]
									f=codecs.open('PK.json','w','utf-8')
									json.dump(stop["PK"], f, sort_keys=True, indent=4,ensure_ascii=False)
								else:
									client.sendMessage(msg.to, '既にオフにされています。')
							##############################################
							if msg.text == "招待保護:オン":
								if msg.to in stop['PP']:
									client.sendMessage(msg.to, "既に保護しています。")
								else:
									client.sendMessage(msg.to, "招待保護をオンにしました。")
									stop['PP'][msg.to] = msg._from
									f=codecs.open('PP.json','w','utf-8')
									json.dump(stop["PP"], f, sort_keys=True, indent=4,ensure_ascii=False)
							##############################################
							if msg.text == "招待保護:オフ":
								if msg.to in stop['PP']:
									client.sendMessage(msg.to, "招待保護をオフにしました。")
									del stop['PP'][msg.to]
									f=codecs.open('PP.json','w','utf-8')
									json.dump(stop["PP"], f, sort_keys=True, indent=4,ensure_ascii=False)
								else:
									client.sendMessage(msg.to,"既にオフにされています。")
							##############################################
							if msg.text == "グル名保護:オン":
								if msg.to in stop['PN']:
									client.sendMessage(msg.to, '既に保護されています。')
								else:
									stop['PN'][msg.to] = client.getGroup(msg.to).name
									f=codecs.open('PN.json','w','utf-8')
									json.dump(stop["PN"], f, sort_keys=True, indent=4,ensure_ascii=False)
									client.sendMessage(msg.to, 'グル名保護をオンにしました。')
							##############################################
							if msg.text == "グル名保護:オフ":
								if msg.to in stop['PN']:
									client.sendMessage(msg.to, 'グル名保護をオフにしました。')
									del stop['PN'][msg.to]
									f=codecs.open('PN.json','w','utf-8')
									json.dump(stop["PN"], f, sort_keys=True, indent=4,ensure_ascii=False)
								else:
									client.sendMessage(msg.to, '既にオフにされています。')
							##############################################
							if msg.text == "グル画保護:オン":
								if msg.to in stop['PI']:
									client.sendMessage(msg.to, '既に保護されています。')
								else:
									client.sendMessage(msg.to, 'グル画保護をオンにしました。')
									group = client.getGroup(msg.to)
									url = "http://dl.profile.line-cdn.net/" + group.pictureStatus
									urllib.request.urlretrieve(url,msg.to + ".png")
									stop['PI'][msg.to] = True
									f=codecs.open('PI.json','w','utf-8')
									json.dump(stop["PI"], f, sort_keys=True, indent=4,ensure_ascii=False)
							##############################################
							if msg.text == "グル画保護:オフ":
								if msg.to in stop['PI']:
									client.sendMessage(msg.to, 'グル画保護をオフにしました。')
									os.remove(msg.to + '.png')
									del stop['PI'][msg.to]
									f=codecs.open('PI.json','w','utf-8')
									json.dump(stop["PI"], f, sort_keys=True, indent=4,ensure_ascii=False)
								else:
									client.sendMessage(msg.to, '既にオフにされています。')
							##############################################
							if "ブラリス:オン" == msg.text:
								if stop["bls"] == True:
									client.sendMessage(msg.to,"既にオンにされています。")
								else:
									stop["bls"] = True
									client.sendMessage(msg.to,"ブラリス機能をオンにしました。")
							##############################################
							if "ブラリス:オフ" == msg.text:
								if stop["bls"] == False:
									client.sendMessage(msg.to,"既にオフにされています。")
								else:
									stop["bls"] = False
									client.sendMessage(msg.to,"ブラリス機能をオフにしました。")
							##############################################
							if "連絡先:オン" == msg.text:
								if stop["contact"] == True:
									client.sendMessage(msg.to,"既にオンにされています。")
								else:
									stop["contact"] = True
									client.sendMessage(msg.to,"連絡先情報をオンにしました。")
							##############################################
							if "連絡先:オフ" == msg.text:
								if stop["contact"] == False:
									client.sendMessage(msg.to,"既にオフにされています。")
								else:
									stop["contact"] = False
									client.sendMessage(msg.to,"連絡先情報をオフにしました。")
							##############################################
							if "自動追加:オン" == msg.text:
								if stop["aaf"] == True:
									client.sendMessage(msg.to,"既にオンにされています。")
								else:
									stop["aaf"] = True
									client.sendMessage(msg.to,"自動追加をオンにしました。")
							##############################################
							if "自動追加:オフ" == msg.text:
								if stop["aaf"] == False:
									client.sendMessage(msg.to,"既にオフにされています。")
								else:
									stop["aaf"] = False
									client.sendMessage(msg.to,"自動追加をオフにしました。")
							##############################################
							if "追加挨拶変更:" in msg.text:
								text = msg.text.replace("追加挨拶変更:","")
								if text in [""," ","\n",None]:
									client.sendMessage(msg.to,"変更できませんでした。")
								else:
									stop["aam"] = text
									client.sendMessage(msg.to,"[%s]\nに変更しました。" % text)
							##############################################
							if "追加挨拶:オン" == msg.text:
								if stop["aafm"] == True:
									client.sendMessage(msg.to,"既にオンにされています。")
								else:
									stop["aafm"] = True
									client.sendMessage(msg.to,"追加挨拶をオンにしました。")
							##############################################
							if "追加挨拶:オフ" == msg.text:
								if stop["aafm"] == False:
									client.sendMessage(msg.to,"既にオフにされています。")
								else:
									stop["aafm"] = False
									client.sendMessage(msg.to,"追加挨拶をオフにしました。")
							##############################################
							if "自動参加:オン" == msg.text:
								if stop["aj"] == True:
									client.sendMessage(msg.to,"既にオンにされています。")
								else:
									stop["aj"] = True
									client.sendMessage(msg.to,"自動参加をオンにしました。")
							##############################################
							if "自動参加:オフ" == msg.text:
								if stop["aj"] == False:
									client.sendMessage(msg.to,"既にオフにされています。")
								else:
									stop["aj"] = False
									client.sendMessage(msg.to,"自動参加をオフにしました。")
							##############################################
							if "参加挨拶変更:" in msg.text:
								text = msg.text.replace("参加挨拶変更:","")
								if text in [""," ","\n",None]:
									client.sendMessage(msg.to,"変更できない文字列です。")
								else:
									stop["ajm"] = text
									client.sendMessage(msg.to,"[%s]\nに変更しました" % text)
							#############################################
							if "参加挨拶:オン" == msg.text:
								if stop["ajfm"] == True:
									client.sendMessage(msg.to,"既にオンにされています。")
								else:
									stop["ajfm"] = True
									client.sendMessage(msg.to,"参加挨拶をオンにしました。")
							#############################################
							if "参加挨拶:オフ" == msg.text:
								if stop["ajfm"] == False:
									client.sendMessage(msg.to,"既にオフにされています。")
								else:
									stop["ajfm"] = False
									client.sendMessage(msg.to,"参加挨拶をオフにしました。")
							#############################################
							if "強制退出:オン" == msg.text:
								if stop["arl"] == True:
									client.sendMessage(msg.to,"既にオンにされています。")
								else:
									stop["arl"] = True
									client.sendMessage(msg.to,"自動強制退出をオンにしました。")
							#############################################
							if "強制退出:オフ" == msg.text:
								if stop["arl"] == False:
									client.sendMessage(msg.to,"既にオフにされています。")
								else:
									stop["arl"] = False
									client.sendMessage(msg.to,"自動強制退出をオフしました。")
							#############################################
							if "共有:オン" == msg.text:
								if stop["noto"] == True:
									client.sendMessage(msg.to,"既にオンにされています。")
								else:
									stop["noto"] = True
									client.sendMessage(msg.to,"共有をオンにしました。")
							#############################################
							if "共有:オフ" == msg.text:
								if stop["noto"] == False:
									client.sendMessage(msg.to,"既にオフにされています。")
								else:
									stop["noto"] = False
									client.sendMessage(msg.to,"共有をオフにしました。")
							#############################################
							if "設定確認" == msg.text:
								mtn = ""
								mtn += "追加挨拶 : \n\n%s\n\n" % stop['aam']
								mtn += "参加挨拶 : \n\n%s\n\n" % stop['ajm']
								if stop['aj'] == False:
									mtn += "自動参加 :off\n"
								else:
									mtn += "自動参加 :on\n"
								if stop['aaf'] == False:
									mtn += "自動追加 :off\n"
								else:
									mtn += "自動追加 :on\n"
								if stop['arl'] == False:
									mtn += "強制 :off\n"
								else:
									mtn += "強制 :on\n"
								if stop['noto'] == False:
									mtn += "共有 :off\n"
								else:
									mtn += "共有 :on\n"
								if stop['contact'] == False:
									mtn += "連絡先 :off\n"
								else:
									mtn += "連絡先 :on\n"
								if stop['ajfm'] == False:
									mtn += "参加挨拶 :off\n"
								else:
									mtn += "挨拶 :on\n"
								if stop['aafm'] == False:
									mtn += "追加挨拶 :off"
								else:
									mtn += "追加挨拶 :on"
								client.sendMessage(msg.to, mtn)
                            #############################################
							if msg.text == "速度":
							    start = time.time()
							    client.sendMessage(msg.to, "うーん、この botの速度は…")
							    elapsed_time = time.time() - start
							    client.sendMessage(msg.to, "≫%ssecかな〜" % (elapsed_time))
							##############################################
							if msg.text == '停止':
								f=codecs.open('PP.json','w','utf-8')
								json.dump(stop["PP"], f, sort_keys=True, indent=4,ensure_ascii=False)
								f=codecs.open('PN.json','w','utf-8')
								json.dump(stop["PN"], f, sort_keys=True, indent=4,ensure_ascii=False)
								f=codecs.open('PI.json','w','utf-8')
								json.dump(stop["PI"], f, sort_keys=True, indent=4,ensure_ascii=False)
								f=codecs.open('black.json','w','utf-8')
								json.dump(stop["bls"], f, sort_keys=True, indent=4,ensure_ascii=False)
								client.sendMessage(msg.to, '半botを終了します。')
								sys.exit(0)
							##############################################
							if "招待URL:" in msg.text:
								gid = msg.text.replace("@招待URL:","")
								gurl = client.reissueGroupTicket(gid)
								client.sendMessage(msg.to,"line://ti/g/" + gurl)
							##############################################
							if msg.text == "招待URL生成":
								g = client.getGroup(msg.to)
								if g.preventJoinByTicket == False:
									client.sendMessage(msg.to, "参加可能状態\n\nline://ti/g/" + client._client.reissueGroupTicket(msg.to))
								else:
									client.sendMessage(msg.to, "参加拒否状態\n\nline://ti/g/" + client._client.reissueGroupTicket(msg.to))
							##############################################
							if msg.text == "招待URL許可":
								g = client.getGroup(msg.to)
								if g.preventJoinByTicket == False:
									client.sendMessage(msg.to, '既に許可されていますね。')
								else:
									g.preventJoinByTicket = False
									client.updateGroup(g)
									client.sendMessage(msg.to, 'url招待を許可しました。')
							##############################################
							if msg.text == "招待URL拒否":
								g = client.getGroup(msg.to)
								if g.preventJoinByTicket == True:
									client.sendMessage(msg.to, '既に拒否られてますね。')
								else:
									g.preventJoinByTicket = True
									client.updateGroup(g)
									client.sendMessage(msg.to, 'url招待を拒否しました。')
							##############################################
							if "ブラリス追加" == msg.text:
								if stop['blc'] == True:
									client.sendMessage(msg.to,"登録するアカウントを送信してください。")
									stop["wb"] = True
								else:
									client.sendMessage(msg.to,"ブラックリスト機能をオンにしてください")
							if "ブラリス追加" in msg.text:
								if msg.contentMetadata is not None:
									targets = []
									key = eval(msg.contentMetadata["MENTION"])
									key["MENTIONEES"][0]["M"]
									for x in key["MENTIONEES"]:
										targets.append(x["M"])
									for target in targets:
										if target in stop["bls"]:
											client.sendMessage(msg.to,"既に登録されています。")
										else:
											stop["bls"][target] = True
									client.sendMessage(msg.to,"ブラリスに登録しました。")
									f = codecs.open('black.json','w','utf-8')
									json.dump(stop["bls"], f, sort_keys=True, indent=4,ensure_ascii=False)
									f.close()
							##############################################
							if "ブラリス解除" == msg.text:
								if stop['blc'] == True:
									client.sendMessage(msg.to,"アカウントを送信してください。")
									stop["db"] = True
								else:
									client.sendMessage(msg.to,"ブラックリスト機能をオンにしてください")
							if "ブラリス解除" in msg.text:
								if msg.contentMetadata is not None:
									targets = []
									key = eval(msg.contentMetadata["MENTION"])
									key["MENTIONEES"][0]["M"]
									for x in key["MENTIONEES"]:
										targets.append(x["M"])
									for target in targets:
										if target in stop["bls"]:
											del stop["bls"][target]
										else:
											client.sendMessage(msg.to,"登録されてません。")
									client.sendMessage(msg.to,"ブラリスを解除しました。")
									f = codecs.open('black.json','w','utf-8')
									json.dump(stop["bls"], f, sort_keys=True, indent=4,ensure_ascii=False)
									f.close()
							##############################################
							if "全ブラリス確認" == msg.text:
								if stop["bls"] == {}:
									client.sendMessage(msg.to,"ブラックリストに登録している人はいません。")
								else:
									client.sendMessage(msg.to,"以下がブラックリストです。")
									mc = ""
									for mi_d in stop["bls"]:
										try:
											mc += "・" +client.getContact(mi_d).displayName + "\n"
										except Exception as error:
											client.sendMessage(msg.to,str(error))
									client.sendMessage(msg.to,mc)
							##############################################
							if "ブラリス確認" == msg.text:
							 	group = client.getGroup(msg.to)
							 	gMembMids = [contact.mid for contact in group.members]
							 	matched_list = []
							 	for tag in stop["bls"]:
							 		matched_list+=[str for str in gMembMids if str == tag]
							 	cocoa = ""
							 	for mm in matched_list:
							 		try:
							 			cocoa += client.getContact(mm).displayName + "\n"
							 		except Exception as error:
							 			try:
							 				client.sendMessage(msg.to,str(error))
							 			except:
							 				pass
							 	if cocoa == "":
							 		client.sendMessage(msg.to,"ブラックリストユーザーはいません。")
							 	else:
							 		client.sendMessage(msg.to,cocoa + "がブラックリストです。")
							##############################################
							if "ブラリス排除" == msg.text:
								group = client.getGroup(msg.to)
								gMembMids = [contact.mid for contact in group.members]
								matched_list = []
								for tag in stop["bls"]:
								    matched_list+=[str for str in gMembMids if str == tag]
								if matched_list == []:
								    client.sendMessage(msg.to,"ブラックリストユーザーはいません。")
								for jj in matched_list:
									try:
									    client.kickoutFromGroup(msg.to,[jj])
									except:
										client.kickoutFromGroup(msg.to,[jj])
								client.sendMessage(msg.to,"kick完了。")
							##############################################
							if "Nk:" in msg.text:
								name = msg.text.replace("Nk:",'')
								gs = client.getGroup(msg.to)
								targets = []
								for g in gs.members:
									if name in g.displayName:
										targets.append(g.mid)
								if targets == []:
									client.sendMessage(msg.to,"Not Found.")
								else:
									for target in targets:
										try:
											client.kickoutFromGroup(msg.to,[target])
										except:
											client.sendMessage(msg.to,'Error')
							##############################################
							if msg.text in ["全ブラリス削除"]:
								stop["bls"] = {}
								client.sendMessage(msg.to,"全てのブラリスを削除しました。")
							##############################################
							if "Mk" in msg.text:
								if msg.contentMetadata is not None:
									targets = []
									key = eval(msg.contentMetadata["MENTION"])
									key["MENTIONEES"][0]["M"]
									for x in key["MENTIONEES"]:
										targets.append(x["M"])
									for target in targets:
										try:
											client.kickoutFromGroup(msg.to,[target])
										except:
											client.sendMessage(msg.to,"Error")
								else:
									pass

						if msg.contentType == 13:
							if stop['contact'] == True:
								contact = client.getContact(msg.contentMetadata["mid"])
								client.sendMessage(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus)
							if stop['blc'] == True:
								if stop["wb"] == True:
									if msg.contentMetadata["mid"] in stop["bls"]:
										client.sendMessage(msg.to,"既に登録されています。")
										stop["wb"] = False
									else:
										stop["bls"][msg.contentMetadata["mid"]] = True
										stop["wb"] = False
										client.sendMessage(msg.to,"ブラリス追加します")
										f=codecs.open('black.json','w','utf-8')
										json.dump(stop["bls"], f, sort_keys=True, indent=4,ensure_ascii=False)
								if stop["db"] == True:
									if msg.contentMetadata["mid"] in stop["bls"]:
										del stop["bls"][msg.contentMetadata["mid"]]
										client.sendMessage(msg.to,"ブラリス解除します")
										stop["db"] = False
										f=codecs.open('black.json','w','utf-8')
										json.dump(stop["bls"], f, sort_keys=True, indent=4,ensure_ascii=False)
									else:
										stop["db"] = False
										client.sendMessage(msg.to,"登録されてません。")

						if msg.contentType == 16:
							if stop['noto'] == True:
								if 'text' not in msg.contentMetadata:
									if 'mediaOid' in msg.contentMetadata:
										Object = msg.contentMetadata['mediaOid'].replace("svc=myhome|sid=h|","")
										if msg.contentMetadata['mediaType'] == 'V':
											if msg.contentMetadata['serviceType'] == 'GB':
												client.sendMessage(msg.to, client.getContact(msg._from).displayName + "さんがノートに投稿しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&oid=" + msg.contentMetadata['mediaOid'] + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
											else:
												client.sendMessage(msg.to, client.getContact(msg._from).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&" + Object + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
										else:
											if msg.contentMetadata['serviceType'] == 'GB':
												client.sendMessage(msg.to, client.getContact(msg._from).displayName + "さんがノートに投稿しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
											else:
												client.sendMessage(msg.to, client.getContact(msg._from).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
									elif 'stickerId' in msg.contentMetadata:
										if msg.contentMetadata['serviceType'] == 'GB':
											client.sendMessage(msg.to, client.getContact(msg._from).displayName + "さんがノートに投稿しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
										else:
											client.sendMessage(msg.to, client.getContact(msg._from).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
									else:
										if msg.contentMetadata['serviceType'] == 'GB':
											client.sendMessage(msg.to, client.getContact(msg._from).displayName + "さんがノートに投稿しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'])
										else:
											client.sendMessage(msg.to, client.getContact(msg._from).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'])
								else:
									if 'mediaOid' in msg.contentMetadata:
										Object = msg.contentMetadata['mediaOid'].replace("svc=myhome|sid=h|","")
										if msg.contentMetadata['mediaType'] == 'V':
											if msg.contentMetadata['serviceType'] == 'GB':
												client.sendMessage(msg.to, client.getContact(msg._from).displayName + "さんがノートに投稿しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&oid=" + msg.contentMetadata['mediaOid'] + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
											else:
												client.sendMessage(msg.to, client.getContact(msg._from).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&" + Object + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
										else:
											if msg.contentMetadata['serviceType'] == 'GB':
												client.sendMessage(msg.to, client.getContact(msg._from).displayName + "さんがノートに投稿しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl']+ "\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
											else:
												client.sendMessage(msg.to, client.getContact(msg._from).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl']+ "\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
									elif 'stickerId' in msg.contentMetadata:
										if msg.contentMetadata['serviceType'] == 'GB':
											client.sendMessage(msg.to, client.getContact(msg._from).displayName + "さんがノートに投稿しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
										else:
											client.sendMessage(msg.to, client.getContact(msg._from).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
									else:
										if msg.contentMetadata['serviceType'] == 'GB':
											client.sendMessage(msg.to, client.getContact(msg._from).displayName + "さんがノートに投稿しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'])
										else:
											client.sendMessage(msg.to, client.getContact(msg._from).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました！\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'])
							
					except Exception as e:
						client.log("[SEND_MESSAGE] ERROR : " + str(e))
				poll.setRevision(op.revision)

	except Exception as e:
		client.log("[SINGLE_TRACE] ERROR : " + str(e))