(function(g){var window=this;var xza=function(a,b){var c=[];g.ri(b,function(a){try{var b=g.FD.prototype.o.call(this,a,!0)}catch(f){if("Storage: Invalid value was encountered"==f)return;throw f;}g.t(b)?g.ED(b)&&c.push(a):c.push(a)},a);
return c},yza=function(a,b){var c=xza(a,b);
(0,g.G)(c,function(a){g.FD.prototype.remove.call(this,a)},a)},zza=function(){var a=g.mH;
yza(a,a.g.Xd(!0))},P7=function(a,b){g.C0.call(this,g.U("YTP_MDX_TITLE"),0,a,b);
this.T=a;this.F={};this.P(a,"onMdxReceiversChange",this.I);this.P(a,"presentingplayerstatechange",this.I);this.I()},Aza=function(){return"function"==typeof window.__onGCastApiAvailable?window.__onGCastApiAvailable:null},Bza=function(a,b){var c=new window.XMLHttpRequest;
c.onreadystatechange=function(){4==c.readyState&&200==c.status&&b(!0)};
c.onerror=function(){b(!1)};
try{c.open("GET",a,!0),c.send()}catch(d){b(!1)}},Q7=function(){var a=Aza();
a&&a(!1,"No cast extension found")},R7=function(a,b,c){var d=window.document.createElement("script");
d.onerror=b;c&&(d.onload=c);d.src=a;(window.document.head||window.document.documentElement).appendChild(d)},S7=function(a){if(a>=g.qsa.length)Q7();
else{var b=g.qsa[a],c="chrome-extension://"+b+g.nsa;0<=g.Z1.indexOf(b)?Bza(c,function(d){d?(window.chrome.cast=window.chrome.cast||{},window.chrome.cast.extensionId=b,R7(c,Q7)):S7(a+1)}):R7(c,function(){S7(a+1)})}},T7=function(a){return 0<=window.navigator.userAgent.indexOf(a)},Cza=function(){if(g.osa){var a=2,b=Aza(),c=function(){a--;
0==a&&b&&b(!0)};
window.__onGCastApiAvailable=c;R7("//www.gstatic.com/cast/sdk/libs/sender/1.0/cast_framework.js",Q7,c)}},Dza=function(){if(T7("CriOS")){var a=window.__gCrWeb&&window.__gCrWeb.message&&window.__gCrWeb.message.invokeOnHost;
if(a){Cza();a({command:"cast.sender.init"});return}}if(!window.chrome||T7("Edge"))Q7();else if(Cza(),T7("Android")&&T7("Chrome/")&&window.navigator.presentation){a="";var b=g.Oh();55<=b?a="55":50<=b&&(a="50");R7("//www.gstatic.com/eureka/clank"+a+g.nsa,Q7)}else S7(0)},Eza=function(a){g.FG[a]&&(a=g.FG[a],(0,g.G)(a,function(a){g.DG[a]&&delete g.DG[a]}),a.length=0)},Fza=function(a){var b=g.CG();
if(b)if(b.clear(a),a)Eza(a);else for(var c in g.FG)Eza(c)},Gza=function(a){this.port=this.domain="";
this.g="/api/lounge";this.o=!0;a=a||window.document.location.href;var b=g.Hg(a)||"";b&&(this.port=":"+b);this.domain=g.Gg(a)||"";a=g.Hb;0<=a.search("MSIE")&&(a=a.match(/MSIE ([\d.]+)/)[1],0>g.Xa(a,"10.0")&&(this.o=!1))},Hza=function(a){return(0,g.J)(a,function(a){return{key:a.id,
name:a.name}})},Iza=function(){var a=window.document.createElement("a");
g.Xc(a,"https://www.gstatic.com/cv/js/sender/v1/cast_sender.js");a=a.href.replace(/^[a-zA-Z]+:\/\//,"//");return"js-"+g.Ya(a)},Jza=function(a,b){var c=g.Cd("SCRIPT");
c.id=a;c.onload=function(){b&&(0,window.setTimeout)(b,0)};
c.onreadystatechange=function(){switch(c.readyState){case "loaded":case "complete":c.onload()}};
g.Yc(c,g.ce("https://www.gstatic.com/cv/js/sender/v1/cast_sender.js"));var d=window.document.getElementsByTagName("head")[0]||window.document.body;d.insertBefore(c,d.firstChild);return c},Kza=function(){var a=Iza(),b=window.document.getElementById(a),c=b&&g.SF(b,"loaded");
c||b&&!c||(b=Jza(a,function(){g.SF(b,"loaded")||(g.TF(b,"loaded","true"),g.IG(a),g.WE(g.Fa(Fza,a),0))}))},Lza=function(){var a=0<=g.Hb.search(/\ (CrMo|Chrome|CriOS)\//);
return g.sL||a},U7=function(a){g.CH("cloudview",a)},V7=function(a){g.ua("yt.mdx.remote.cloudview.initializing_",a,void 0)},W7=function(){return g.x("yt.mdx.remote.cloudview.instance_")},Mza=function(a,b,c,d){var e=!1;
W7()||(a=new g.DI(a,b,c,d),a.subscribe("yt-remote-cast2-availability-change",function(a){g.oH("yt-remote-cast-available",a);g.KG("yt-remote-cast2-availability-change",a)}),a.subscribe("yt-remote-cast2-receiver-selected",function(a){U7("onReceiverSelected: "+a.friendlyName);
g.oH("yt-remote-cast-receiver",a);g.KG("yt-remote-cast2-receiver-selected",a)}),a.subscribe("yt-remote-cast2-receiver-resumed",function(a){U7("onReceiverResumed: "+a.friendlyName);
g.oH("yt-remote-cast-receiver",a)}),a.subscribe("yt-remote-cast2-session-change",function(a){U7("onSessionChange: "+g.KH(a));
a||g.qH("yt-remote-cast-receiver");g.KG("yt-remote-cast2-session-change",a)}),g.ua("yt.mdx.remote.cloudview.instance_",a,void 0),e=!0);
U7("cloudview.createSingleton_: "+e);return e},Nza=function(a){U7("setApiReady_ "+a);
g.ua("yt.mdx.remote.cloudview.apiReady_",a,void 0)},Oza=function(){U7("dispose");
var a=W7();a&&a.dispose();g.ua("yt.mdx.remote.cloudview.instance_",null,void 0);Nza(!1);g.HG(X7);X7.length=0},Y7=function(){return!!g.pH("yt-remote-cast-installed")},Pza=function(){var a=g.pH("yt-remote-cast-receiver");
return a?a.friendlyName:null},Qza=function(){U7("clearCurrentReceiver");
g.qH("yt-remote-cast-receiver")},Z7=function(a){g.CH("cloudview",a)},Rza=function(){return Y7()?W7()?W7().getCastSession():(Z7("getCastSelector: Cast is not initialized."),null):(Z7("getCastSelector: Cast API is not installed!"),null)},$7=function(){return!!g.x("yt.mdx.remote.cloudview.apiReady_")},a8=function(){Y7()?W7()?$7()?(U7("Requesting cast selector."),W7().requestSession()):(U7("Wait for cast API to be ready to request the session."),X7.push(g.GG("yt-remote-cast2-api-ready",a8))):Z7("requestCastSelector: Cast is not initialized."):
Z7("requestCastSelector: Cast API is not installed!")},b8=function(a,b){$7()?W7().setConnectedScreenStatus(a,b):Z7("setConnectedScreenStatus called before ready.")},c8=function(a){U7("setCastInstalled_ "+a);
g.oH("yt-remote-cast-installed",a)},Sza=function(a,b){W7().init(a,b)},Tza=function(a,b){c8(!0);
V7(!1);Sza(a,function(a){a?(Nza(!0),g.IG("yt-remote-cast2-api-ready")):(Z7("Failed to initialize cast API."),c8(!1),g.qH("yt-remote-cast-available"),g.qH("yt-remote-cast-receiver"),Oza());b(a)})},Uza=function(a,b,c,d,e,f,k){Lza()?Mza(b,e,f,k)&&(V7(!0),window.chrome&&window.chrome.cast&&window.chrome.cast.isAvailable?Tza(a,c):(window.__onGCastApiAvailable=function(b,d){b?Tza(a,c):(Z7("Failed to load cast API: "+d),c8(!1),V7(!1),g.qH("yt-remote-cast-available"),g.qH("yt-remote-cast-receiver"),Oza(),
c(!1))},d?window.spf?window.spf.script.load("https://www.gstatic.com/cv/js/sender/v1/cast_sender.js","",void 0):Kza():Dza())):U7("Cannot initialize because not running Chrome")},e8=function(a,b){g.tG.call(this);
this.g=0;this.B=a;this.D=[];this.C=new g.TB;this.A=this.o=null;this.I=(0,g.z)(this.dP,this);this.F=(0,g.z)(this.Cl,this);this.G=(0,g.z)(this.cP,this);this.J=(0,g.z)(this.qP,this);var c=0;a?(c=a.getProxyState(),3!=c&&(a.subscribe("proxyStateChange",this.bv,this),Vza(this))):c=3;0!=c&&(b?this.bv(c):g.WE((0,g.z)(function(){this.bv(c)},this),0));
var d=Rza();d&&d8(this,d);this.subscribe("yt-remote-cast2-session-change",this.J)},f8=function(a){return new g.JI(a.B.getPlayerContextData())},Wza=function(a,b,c,d,e){var f=f8(a),k=e||f.listId;
d=d||0;var l={videoId:b,currentIndex:d};g.NI(f,b,d);g.t(c)&&(g.LI(f,c),l.currentTime=c);g.t(k)&&(l.listId=k);g8(a,"setPlaylist",l);e||h8(a,f)},Vza=function(a){(0,g.G)("nowAutoplaying autoplayDismissed remotePlayerChange remoteQueueChange autoplayModeChange autoplayUpNext previousNextChange".split(" "),function(a){this.D.push(this.B.subscribe(a,g.Fa(this.uR,a),this))},a)},Xza=function(a){(0,g.G)(a.D,function(a){this.B.unsubscribeByKey(a)},a);
a.D.length=0},i8=function(a,b){50>a.C.Jc()&&g.VB(a.C,b)},j8=function(a,b,c){var d=f8(a);
g.LI(d,c);-1E3!=d.g&&(d.g=b);h8(a,d)},g8=function(a,b,c){a.B.sendMessage(b,c)},h8=function(a,b){Xza(a);
a.B.setPlayerContextData(g.OI(b));Vza(a)},d8=function(a,b){a.A&&(a.A.removeUpdateListener(a.I),a.A.removeMediaListener(a.F),a.Cl(null));
a.A=b;a.A&&(k8("Setting cast session: "+a.A.sessionId),a.A.addUpdateListener(a.I),a.A.addMediaListener(a.F),a.A.media.length&&a.Cl(a.A.media[0]))},Yza=function(a){var b=a.o.media,c=a.o.customData;
if(b&&c){var d=f8(a);b.contentId!=d.videoId&&k8("Cast changing video to: "+b.contentId);d.videoId=b.contentId;d.g=c.playerState;g.LI(d,a.o.getEstimatedTime());h8(a,d)}else k8("No cast media video. Ignoring state update.")},k8=function(a){g.CH("CP",a)},l8=function(a,b,c){return(0,g.z)(function(a){this.Zb("Failed to "+b+" with cast v2 channel. Error code: "+a.code);
a.code!=window.chrome.cast.ErrorCode.TIMEOUT&&(this.Zb("Retrying "+b+" using MDx browser channel."),g8(this,b,c))},a)},m8=function(a){g.PH.call(this,"ScreenServiceProxy");
this.ed=a;this.o=[];this.o.push(this.ed.$_s("screenChange",(0,g.z)(this.MU,this)));this.o.push(this.ed.$_s("onlineScreenChange",(0,g.z)(this.aR,this)))},n8=function(){return g.x("yt.mdx.remote.currentScreenId_")},o8=function(a){g.CH("remote",a)},p8=function(a){g.ua("yt.mdx.remote.connectData_",a,void 0)},q8=function(){return g.x("yt.mdx.remote.channelParams_")||{}},Zza=function(){var a=q8();
if(g.Xb(a)){a=g.VH();var b=g.pH("yt-remote-session-name")||"",c=g.pH("yt-remote-session-app")||"";a={device:"REMOTE_CONTROL",id:a,name:b,app:c,"mdx-version":3};g.ua("yt.mdx.remote.channelParams_",a,void 0)}},$za=function(a){a?(g.oH("yt-remote-session-app",a.app),g.oH("yt-remote-session-name",a.name)):(g.qH("yt-remote-session-app"),g.qH("yt-remote-session-name"));
g.ua("yt.mdx.remote.channelParams_",a,void 0)},r8=function(){return g.x("yt.mdx.remote.connection_")},s8=function(){var a=r8();
return!!a&&3!=a.getProxyState()},aAa=function(){return g.x("yt.mdx.remote.connectData_")},u8=function(){if(!t8){var a=g.x("yt.mdx.remote.screenService_");
t8=a?new m8(a):null}return t8},v8=function(){var a=g.WH();
if(!a)return null;var b=u8().ge();return g.OH(b,a)},w8=function(){var a=n8();
if(!a)return null;var b=u8().ge();return g.OH(b,a)},bAa=function(){var a=u8().ed.$_gos();
var b=w8();b&&r8()&&(g.NH(a,b)||a.push(b));return Hza(a)},cAa=function(){var a=bAa(),b=w8();
b||(b=v8());return g.eb(a,function(a){return b&&g.HH(b,a.key)?!0:!1})},x8=function(){var a=cAa();
!a&&Y7()&&Pza()&&(a={key:"cast-selector-receiver",name:Pza()});return a},dAa=function(){var a=bAa();
Y7()&&g.pH("yt-remote-cast-available")&&a.push({key:"cast-selector-receiver",name:"Cast..."});return a},eAa=function(a){g.ua("yt.mdx.remote.currentScreenId_",a,void 0)},z8=function(a){var b=r8();
p8(null);a||eAa("");g.ua("yt.mdx.remote.connection_",a,void 0);y8&&((0,g.G)(y8,function(b){b(a)}),y8.length=0);
b&&!a?g.KG("yt-remote-connection-change",!1):!b&&a&&g.KG("yt-remote-connection-change",!0)},B8=function(a,b){w8()&&w8();
eAa(a.id);var c=new g.UI(A8,a,q8());c.connect(b,aAa());c.subscribe("beforeDisconnect",function(a){g.KG("yt-remote-before-disconnect",a)});
c.subscribe("beforeDispose",function(){r8()&&z8(null)});
z8(c)},fAa=function(){var a=v8();
a?(o8("Resume connection to: "+g.KH(a)),B8(a,0)):(g.cI(),Qza(),o8("Skipping connecting because no session screen found."))},C8=function(){$7()?W7().stopSession():Z7("stopSession called before API ready.");
var a=r8();a&&(a.disconnect(1),z8(null))},gAa=function(a){o8("remote.onCastSessionChange_: "+g.KH(a));
if(a){var b=w8();b&&b.id==a.id?b8(b.id,"YouTube TV"):(b&&C8(),B8(a,1))}else r8()&&C8()},hAa=function(a){var b={device:"Desktop",
app:"youtube-desktop"};b=g.mE("MDX_CONFIG")||b;g.mH&&zza();g.XH();A8||(A8=new Gza(b?b.loungeApiHost:void 0),g.eI()&&(A8.g="/api/loungedev"));y8||(y8=g.x("yt.mdx.remote.deferredProxies_")||[],g.ua("yt.mdx.remote.deferredProxies_",y8,void 0));Zza();var c=u8();if(!c){var d=new g.pI(A8);g.ua("yt.mdx.remote.screenService_",d,void 0);c=u8();var e=!1,f=void 0,k=void 0,l=!1;b&&(e=!!b.loadCastApiSetupScript,f=b.appId,k=b.theme,l=!!b.disableDial);Uza(a,d,function(a){a?n8()&&b8(n8(),"YouTube TV"):d.subscribe("onlineScreenChange",
function(){g.KG("yt-remote-receiver-availability-change")})},e,f,k,l)}b&&!g.x("yt.mdx.remote.initialized_")&&(g.ua("yt.mdx.remote.initialized_",!0,void 0),o8("Initializing: "+g.yg(b)),D8.push(g.GG("yt-remote-cast2-availability-change",function(){g.KG("yt-remote-receiver-availability-change")})),D8.push(g.GG("yt-remote-cast2-receiver-selected",function(){p8(null);
g.KG("yt-remote-auto-connect","cast-selector-receiver")})),D8.push(g.GG("yt-remote-cast2-receiver-resumed",function(){g.KG("yt-remote-receiver-resumed","cast-selector-receiver")})),D8.push(g.GG("yt-remote-cast2-session-change",gAa)),D8.push(g.GG("yt-remote-connection-change",function(a){a?b8(n8(),"YouTube TV"):v8()||(b8(null,null),Qza())})),a=q8(),b.isAuto&&(a.id+="#dial"),g.zF("desktop_enable_autoplay")&&(a.capabilities=["atp"]),a.name=b.device,a.app=b.app,(k=b.theme)&&(a.theme=k),o8(" -- with channel params: "+
g.yg(a)),$za(a),c.start(),n8()||fAa())},E8=function(a,b,c){g.L.call(this);
this.F=a;this.T=b;this.o=new g.qG(this);g.M(this,this.o);this.o.P(b,"onCaptionsTrackListChanged",this.tQ);this.o.P(b,"captionschanged",this.bP);this.o.P(b,"captionssettingschanged",this.kD);this.o.P(b,"videoplayerreset",this.Mo);this.o.P(b,"mdxautoplaycancel",this.JH);this.N=this.o.P(b,"onVolumeChange",this.EB);this.D=!1;this.g=c;c.subscribe("proxyStateChange",this.RB,this);c.subscribe("remotePlayerChange",this.El,this);c.subscribe("remoteQueueChange",this.Mo,this);c.subscribe("autoplayUpNext",this.rB,
this);c.subscribe("previousNextChange",this.OB,this);c.subscribe("nowAutoplaying",this.GB,this);c.subscribe("autoplayDismissed",this.qB,this);this.suggestion=null;this.G=new g.eR(64);this.A=new g.Jt(this.fD,500,this);g.M(this,this.A);this.B=new g.Jt(this.gD,1E3,this);g.M(this,this.B);this.C={};this.J=new g.Jt(this.HD,1E3,this);g.M(this,this.J);this.I=new g.Dk(this.RL,1E3,this);g.M(this,this.I);this.L=g.y;this.kD();this.Mo();this.El()},F8=function(a,b){var c=a.F,d=a.T.ga().lengthSeconds;
c.I=b||0;c.g.V("progresssync",b,d)},iAa=function(a){F8(a,0);
a.A.stop();G8(a,new g.eR(64))},I8=function(a,b){if(H8(a)&&!a.D){var c=null;
b&&(c={style:a.T.zi()},g.dc(c,b));a.g.YC(a.T.ga().videoId,c);a.C=f8(a.g).o}},J8=function(a,b){var c=a.T.Xf();
c?Wza(a.g,a.T.ga().videoId,b,c.ce(),c.listId.toString()):Wza(a.g,a.T.ga().videoId,b);G8(a,new g.eR(1))},jAa=function(a,b){if(b){var c=a.T.wc("captions","tracklist",{hz:1});
c&&c.length?(a.T.Fd("captions","track",b),a.D=!1):(a.T.sl("captions"),a.D=!0)}else a.T.Fd("captions","track",{})},H8=function(a){return f8(a.g).videoId==a.T.ga().videoId},G8=function(a,b){a.B.stop();
var c=a.G;if(!g.jR(c,b)){var d=g.W(b,2);if(d!=g.W(a.G,2)){var e=a.T;g.u1(e.app,d,e.playerType)}a.G=b;kAa(a.F,c,b)}},K8=function(a){g.Y.call(this,{H:"div",
M:"ytp-remote",K:[{H:"div",M:"ytp-remote-display-status",K:[{H:"div",M:"ytp-remote-display-status-icon",K:[g.rE()]},{H:"div",M:"ytp-remote-display-status-text",K:["{{statustext}}"]}]}]});this.o=new g.wX(this,250);g.M(this,this.o);this.A=a;this.P(a,"presentingplayerstatechange",this.B);lAa(this,g.CW(a))},lAa=function(a,b){if(3==a.A.Va()){var c={RECEIVER_NAME:a.A.wc("remote","currentReceiver").name};
c=g.W(b,128)?g.U("YTP_MDX_STATUS_ERROR_2",c):b.jb()||g.W(b,4)?g.U("YTP_MDX_STATUS_PLAYING_2",c):g.U("YTP_MDX_STATUS_CONNECTED_2",c);a.updateValue("statustext",c);a.o.show()}else a.o.hide()},L8=function(a){g.mX.call(this,a);
this.A={key:g.MH(),name:g.U("YTP_MDX_MY_COMPUTER")};this.C=null;this.D=[];this.J=this.o=null;this.G=[this.A];this.B=this.A;this.F=new g.eR(64);this.I=0;var b=g.vW(a).G;b&&(b=b.A&&b.A.g)&&(b=new P7(a,b),g.M(this,b));b=new K8(a);g.M(this,b);g.SW(a,b.element,4)},kAa=function(a,b,c){a.F=c;
a.g.V("presentingplayerstatechange",new g.oR(c,b))},M8=function(a,b){if(b.key!=a.B.key)if(b.key==a.A.key)C8();
else{a.B=b;var c=a.g.getPlaylistId();var d=a.g.ga(1),e=d.videoId;if(c||e){var f=a.g.Xf();if(f){var k=[];for(var l=0;l<f.getLength();l++)k[l]=f.hc(l).videoId}else k=[e];c={videoIds:k,listId:c,videoId:e,playerParams:d.playerParams,index:Math.max(a.g.lA(),0),currentTime:a.g.getCurrentTime()}}else c=null;o8("Connecting to: "+g.yg(b));"cast-selector-receiver"==b.key?(p8(c||null),$7()?W7().setLaunchParams(c||null):Z7("setLaunchParams called before ready.")):!c&&s8()&&n8()==b.key?g.KG("yt-remote-connection-change",
!0):(C8(),p8(c||null),c=u8().ge(),(c=g.OH(c,b.key))&&B8(c,1))}};
g.p(P7,g.C0);P7.prototype.I=function(){var a=this.T.wc("remote","receivers");a&&1<a.length&&!this.T.wc("remote","quickCast")?(this.F=g.Fb(a,this.B,this),g.D0(this,(0,g.J)(a,this.B)),a=this.T.wc("remote","currentReceiver"),this.mf(this.B(a)),this.enable(!0)):this.enable(!1)};
P7.prototype.B=function(a){return a.key};
P7.prototype.lf=function(a){return"cast-selector-receiver"==a?g.U("YTP_MDX_CAST_SELECTOR"):this.F[a].name};
P7.prototype.td=function(a){g.C0.prototype.td.call(this,a);this.T.Fd("remote","currentReceiver",this.F[a]);this.A.Mb()};
g.h=Gza.prototype;g.h.ii=function(a){var b=this.g;if(g.t(void 0)?0:this.o)b="https://"+this.domain+this.port+this.g;return g.Qg(b+a,{})};
g.h.Zu=function(a,b,c,d){c={format:"JSON",method:"POST",context:this,timeout:5E3,withCredentials:!1,Tb:g.Fa(this.HU,c,!0),onError:g.Fa(this.GU,d),Hd:g.Fa(this.IU,d)};b&&(c.Nb=b,c.headers={"Content-Type":"application/x-www-form-urlencoded"});return g.jF(a,c)};
g.h.HU=function(a,b,c,d){b?a(d):a({text:c.responseText})};
g.h.GU=function(a,b){a(Error("Request error: "+b.status))};
g.h.IU=function(a){a(Error("request timed out"))};
var X7=[];g.B(e8,g.tG);g.h=e8.prototype;g.h.play=function(){1==this.g?(this.o?this.o.play(null,g.y,l8(this,"play")):g8(this,"play"),j8(this,1,g.MI(f8(this))),this.V("remotePlayerChange")):i8(this,this.play)};
g.h.pause=function(){1==this.g?(this.o?this.o.pause(null,g.y,l8(this,"pause")):g8(this,"pause"),j8(this,2,g.MI(f8(this))),this.V("remotePlayerChange")):i8(this,this.pause)};
g.h.SD=function(a){if(1==this.g){if(this.o){var b=f8(this),c=new window.chrome.cast.media.SeekRequest;c.currentTime=a;c.resumeState=b.jb()||3==b.g?window.chrome.cast.media.ResumeState.PLAYBACK_START:window.chrome.cast.media.ResumeState.PLAYBACK_PAUSE;this.o.seek(c,g.y,l8(this,"seekTo",{newTime:a}))}else g8(this,"seekTo",{newTime:a});j8(this,3,a);this.V("remotePlayerChange")}else i8(this,g.Fa(this.SD,a))};
g.h.stop=function(){if(1==this.g){this.o?this.o.stop(null,g.y,l8(this,"stopVideo")):g8(this,"stopVideo");var a=f8(this);a.index=-1;a.videoId="";g.KI(a);h8(this,a);this.V("remotePlayerChange")}else i8(this,this.stop)};
g.h.setVolume=function(a,b){if(1==this.g){var c=f8(this);if(this.A){if(c.volume!=a){var d=Math.round(a)/100;this.A.setReceiverVolumeLevel(d,(0,g.z)(function(){k8("set receiver volume: "+d)},this),(0,g.z)(function(){this.Zb("failed to set receiver volume.")},this))}c.muted!=b&&this.A.setReceiverMuted(b,(0,g.z)(function(){k8("set receiver muted: "+b)},this),(0,g.z)(function(){this.Zb("failed to set receiver muted.")},this))}else{var e={volume:a,
muted:b};-1!=c.volume&&(e.delta=a-c.volume);g8(this,"setVolume",e)}c.muted=b;c.volume=a;h8(this,c)}else i8(this,g.Fa(this.setVolume,a,b))};
g.h.YC=function(a,b){if(1==this.g){var c=f8(this),d={videoId:a};b&&(c.o={trackName:b.name,languageCode:b.languageCode,sourceLanguageCode:b.translationLanguage?b.translationLanguage.languageCode:"",languageName:b.languageName,format:b.format,kind:b.kind},d.style=g.yg(b.style),g.dc(d,c.o));g8(this,"setSubtitlesTrack",d);h8(this,c)}else i8(this,g.Fa(this.YC,a,b))};
g.h.av=function(a,b){if(1==this.g){g8(this,"setAudioTrack",{videoId:a,audioTrackId:b.Rc.id});var c=f8(this);c.audioTrackId=b.Rc.id;h8(this,c)}else i8(this,g.Fa(this.av,a,b))};
g.h.RD=function(a,b){if(1==this.g){if(a&&b){var c=f8(this);g.NI(c,a,b);h8(this,c)}g8(this,"previous")}else i8(this,g.Fa(this.RD,a,b))};
g.h.QD=function(a,b){if(1==this.g){if(a&&b){var c=f8(this);g.NI(c,a,b);h8(this,c)}g8(this,"next")}else i8(this,g.Fa(this.QD,a,b))};
g.h.Dx=function(){1==this.g?g8(this,"dismissAutoplay"):i8(this,this.Dx)};
g.h.dispose=function(){if(3!=this.g){var a=this.g;this.g=3;this.V("proxyStateChange",a,this.g)}e8.Z.dispose.call(this)};
g.h.X=function(){Xza(this);this.B=null;this.C.clear();d8(this,null);e8.Z.X.call(this)};
g.h.bv=function(a){if((a!=this.g||2==a)&&3!=this.g&&0!=a){var b=this.g;this.g=a;this.V("proxyStateChange",b,a);if(1==a)for(;!this.C.isEmpty();)g.WB(this.C).apply(this);else 3==a&&this.dispose()}};
g.h.uR=function(a,b){this.V(a,b)};
g.h.dP=function(a){if(!a)this.Cl(null),d8(this,null);else if(this.A.receiver.volume){a=this.A.receiver.volume;var b=f8(this),c=Math.round(100*a.level||0);if(b.volume!=c||b.muted!=a.muted)k8("Cast volume update: "+a.level+(a.muted?" muted":"")),b.volume=c,b.muted=!!a.muted,h8(this,b)}};
g.h.Cl=function(a){k8("Cast media: "+!!a);this.o&&this.o.removeUpdateListener(this.G);if(this.o=a)this.o.addUpdateListener(this.G),Yza(this),this.V("remotePlayerChange")};
g.h.cP=function(a){a?(Yza(this),this.V("remotePlayerChange")):this.Cl(null)};
g.h.qP=function(){var a=Rza();a&&d8(this,a)};
g.h.Zb=function(a){g.CH("CP",a)};
g.B(m8,g.PH);g.h=m8.prototype;g.h.ge=function(a){return this.ed.$_gs(a)};
g.h.contains=function(a){return!!this.ed.$_c(a)};
g.h.get=function(a){return this.ed.$_g(a)};
g.h.start=function(){this.ed.$_st()};
g.h.Op=function(a,b,c){this.ed.$_a(a,b,c)};
g.h.remove=function(a,b,c){this.ed.$_r(a,b,c)};
g.h.yp=function(a,b,c,d){this.ed.$_un(a,b,c,d)};
g.h.X=function(){for(var a=0,b=this.o.length;a<b;++a)this.ed.$_ubk(this.o[a]);this.o.length=0;this.ed=null;m8.Z.X.call(this)};
g.h.MU=function(){this.V("screenChange")};
g.h.aR=function(){this.V("onlineScreenChange")};
var A8=null,y8=null,D8=[],t8=null;g.p(E8,g.L);g.h=E8.prototype;g.h.X=function(){g.L.prototype.X.call(this);this.A.stop();this.B.stop();this.L();this.g.unsubscribe("proxyStateChange",this.RB,this);this.g.unsubscribe("remotePlayerChange",this.El,this);this.g.unsubscribe("remoteQueueChange",this.Mo,this);this.g.unsubscribe("autoplayUpNext",this.rB,this);this.g.unsubscribe("previousNextChange",this.OB,this);this.g.unsubscribe("nowAutoplaying",this.GB,this);this.g.unsubscribe("autoplayDismissed",this.qB,this);this.g=this.F=null};
g.h.cA=function(a,b){for(var c=[],d=1;d<arguments.length;++d)c[d-1]=arguments[d];if(2!=this.g.g)if(H8(this)){if(1081!=f8(this.g).g||"control_seek"!=a)switch(a){case "control_toggle_play_pause":f8(this.g).jb()?this.g.pause():this.g.play();break;case "control_play":this.g.play();break;case "control_pause":this.g.pause();break;case "control_seek":this.I.mj(c[0],c[1]);break;case "control_subtitles_set_track":I8(this,c[0]);break;case "control_set_audio_track":c=c[0],H8(this)&&this.g.av(this.T.ga().videoId,
c)}}else switch(a){case "control_toggle_play_pause":case "control_play":case "control_pause":J8(this,this.T.getCurrentTime());break;case "control_seek":J8(this,c[0]);break;case "control_subtitles_set_track":I8(this,c[0]);break;case "control_set_audio_track":c=c[0],H8(this)&&this.g.av(this.T.ga().videoId,c)}};
g.h.bP=function(a){this.cA("control_subtitles_set_track",g.Xb(a)?null:a)};
g.h.kD=function(){var a=this.T.wc("captions","track");g.Xb(a)||I8(this,a)};
g.h.EB=function(a){if(H8(this)){this.g.unsubscribe("remotePlayerChange",this.El,this);var b=Math.round(a.volume);a=!!a.muted;var c=f8(this.g);if(b!=c.volume||a!=c.muted)this.g.setVolume(b,a),this.J.start();this.g.subscribe("remotePlayerChange",this.El,this)}};
g.h.tQ=function(){g.Xb(this.C)||jAa(this,this.C);this.D=!1};
g.h.RB=function(a,b){this.B.stop();2==b&&this.gD()};
g.h.El=function(){if(H8(this)){this.A.stop();var a=f8(this.g);switch(a.g){case 1081:G8(this,new g.eR(8));break;case 1:this.fD();G8(this,new g.eR(8));break;case 1083:case 3:G8(this,new g.eR(9));break;case 0:G8(this,new g.eR(2));this.I.stop();F8(this,this.T.ga().lengthSeconds);break;case 1082:G8(this,new g.eR(4));break;case 2:G8(this,new g.eR(4));F8(this,g.MI(a));break;case -1:G8(this,new g.eR(64));break;case -1E3:a={errorCode:"mdx.remoteerror",message:g.U("YTP_MDX_PLAYER_ERROR")},G8(this,new g.eR(128,
a))}a=f8(this.g).o;var b=this.C;(a||b?a&&b&&a.trackName==b.trackName&&a.languageCode==b.languageCode&&a.languageName==b.languageName&&a.format==b.format&&a.kind==b.kind:1)||(this.C=a,jAa(this,a));a=f8(this.g);-1==a.volume||Math.round(this.T.getVolume())==a.volume&&this.T.isMuted()==a.muted||this.J.isActive()||this.HD()}else iAa(this)};
g.h.OB=function(){this.T.V("mdxpreviousnextchange")};
g.h.Mo=function(){H8(this)||iAa(this)};
g.h.JH=function(){this.g.Dx()};
g.h.rB=function(a){a&&(a=g.jF("/watch_queue_ajax",{method:"GET",Zc:{action_get_watch_queue_item:1,video_id:a},Tb:(0,g.z)(this.vS,this)}))&&(this.L=(0,g.z)(a.abort,a))};
g.h.vS=function(a,b){var c=new g.bQ({videoId:b.videoId,title:b.title,author:b.author,murlmq_webp:b.url});this.suggestion=c;this.T.V("mdxautoplayupnext",c)};
g.h.GB=function(a){(0,window.isNaN)(a)||this.T.V("mdxnowautoplaying",a)};
g.h.qB=function(){this.T.V("mdxautoplaycanceled")};
g.h.RL=function(a,b){-1==f8(this.g).g?J8(this,a):b&&this.g.SD(a)};
g.h.HD=function(){if(H8(this)){var a=f8(this.g);this.o.Ca(this.N);a.muted?this.T.mute():this.T.Yf();this.T.setVolume(a.volume);this.N=this.o.P(this.T,"onVolumeChange",this.EB)}};
g.h.fD=function(){this.A.stop();if(!this.g.ka()){var a=f8(this.g);a.jb()&&G8(this,new g.eR(8));F8(this,g.MI(a));this.A.start()}};
g.h.gD=function(){this.B.stop();this.A.stop();var a=this.g.B.getReconnectTimeout();2==this.g.g&&!(0,window.isNaN)(a)&&this.B.start()};g.p(K8,g.Y);K8.prototype.B=function(a){lAa(this,a.state)};g.p(L8,g.mX);g.h=L8.prototype;g.h.create=function(){hAa(g.$N(g.X(this.g)));this.D.push(g.GG("yt-remote-before-disconnect",this.XO,this));this.D.push(g.GG("yt-remote-connection-change",this.ER,this));this.D.push(g.GG("yt-remote-receiver-availability-change",this.PB,this));this.D.push(g.GG("yt-remote-auto-connect",this.CR,this));this.D.push(g.GG("yt-remote-receiver-resumed",this.AR,this));this.PB()};
g.h.load=function(){this.g.Oq();g.mX.prototype.load.call(this);this.C=new E8(this,this.g,this.o);var a=aAa();a=a?a.currentTime:0;var b=s8()?new e8(r8(),void 0):null;0==a&&b&&(a=g.MI(f8(b)));0!=a&&(this.I=a||0,this.g.V("progresssync",a,void 0));kAa(this,this.F,this.F);g.z1(this.g.app,6)};
g.h.unload=function(){this.g.V("mdxautoplaycanceled");this.B=this.A;g.af(this.C,this.o);this.o=this.C=null;g.mX.prototype.unload.call(this);g.z1(this.g.app,5)};
g.h.X=function(){g.HG(this.D);g.mX.prototype.X.call(this)};
g.h.ll=function(a,b){for(var c=[],d=1;d<arguments.length;++d)c[d-1]=arguments[d];this.loaded&&this.C.cA.apply(this.C,[].concat([a],g.pa(c)))};
g.h.wI=function(){return this.loaded?this.C.suggestion:null};
g.h.Mf=function(){return this.o?f8(this.o).Mf:!1};
g.h.hasNext=function(){return this.o?f8(this.o).hasNext:!1};
g.h.getCurrentTime=function(){return this.I};
g.h.tL=function(){var a=f8(this.o),b=this.g.ga();return{allowSeeking:this.g.fd(),clipEnd:b.clipEnd,clipStart:b.clipStart,current:this.getCurrentTime(),displayedStart:-1,duration:a.getDuration(),ingestionTime:a.F?a.C+((0,g.F)()-a.A)/1E3:a.C,isPeggedToLive:1>=(a.F?a.B+((0,g.F)()-a.A)/1E3:a.B)-this.getCurrentTime(),loaded:a.J,seekableEnd:a.F?a.B+((0,g.F)()-a.A)/1E3:a.B,seekableStart:0<a.D?a.D+((0,g.F)()-a.A)/1E3:a.D}};
g.h.uL=function(){this.o&&this.o.QD()};
g.h.vL=function(){this.o&&this.o.RD()};
g.h.XO=function(a){1==a&&(this.J=this.o?f8(this.o):null)};
g.h.ER=function(){var a=s8()?new e8(r8(),void 0):null;if(a){var b=this.B;this.loaded&&this.unload();this.o=a;this.J=null;b.key!=this.A.key&&(this.B=b,this.load())}else g.$e(this.o),this.o=null,this.loaded&&(this.unload(),(a=this.J)&&a.videoId==this.g.ga().videoId&&this.g.jA(a.videoId,g.MI(a)));this.g.V("videodatachange","newdata",this.g.ga(),3)};
g.h.PB=function(){this.G=[this.A].concat(dAa());var a=x8()||this.A;M8(this,a);this.g.va("onMdxReceiversChange")};
g.h.CR=function(){var a=x8();M8(this,a)};
g.h.AR=function(){this.B=x8()};
g.h.sL=function(a,b){switch(a){case "casting":return this.loaded;case "receivers":return this.G;case "currentReceiver":return b&&("cast-selector-receiver"==b.key?a8():M8(this,b)),this.loaded?this.B:this.A;case "quickCast":return 2==this.G.length&&"cast-selector-receiver"==this.G[1].key?(b&&a8(),!0):!1}};
g.h.wL=function(){g8(this.o,"sendDebugCommand",{debugCommand:"stats4nerds "})};
g.h.wd=function(){return!1};g.HZ.remote=L8;})(_yt_player);
