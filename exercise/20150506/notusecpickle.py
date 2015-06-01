shoplistfile = "shoplist.data"

shoplist = ['carrot','toxin','skunk']

f = file(shoplistfile,'w')

f.write(shoplist)

f.close()

del shoplist

f = file(shoplistfile)

f.read()
