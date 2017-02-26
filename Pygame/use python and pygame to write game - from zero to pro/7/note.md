>`pygame.draw`中的函数第一个参数总是一个surface，然后是颜色，再后会是一系列的坐标等。稍有些计算机绘图经验的人就会知道计算机里的坐标，（0，0）代表左上角，而返回值是一个`Rect`对象，包含了绘制的领域，这样你就可以很方便的更新那个部分了。

| 函数     | 作用                             |
|:--------:|:--------------------------------:|
| rect    | 绘制矩形                         |
| polygon | 绘制多边形（三个及三个以上的边） |
| circle  | 绘制圆                           |
| ellipse | 绘制椭圆                         |
| arc     | 绘制圆弧                         |
| line    | 绘制线                           |
| lines   | 绘制一系列的线                   |
| aaline  | 绘制一根平滑的线                 |
| aalines | 绘制一系列平滑的线               |
>注：表格对齐的格式
>第一列 | 第二列 | 第三列
>-------: | :------: | :-------
>右对齐 | 居中 | 左对齐

# pygame.draw.rect
`pygame.draw.rect(Surface,color,Rect,width=0)`
`pygame.draw.rect`在surface上画了一个矩形，除了surface和color，rect接受一个矩形的坐标和线宽参数，如过线宽是0或省略，则填充。另一个方法来画矩形，`fill`方法，事实上fill可能还会快一点，因为**fill由显卡来完成**

# pygame.draw.polygon
`pygame.draw.polygon(Surface,color,pointlist,width=0)`
polygon就是多边形，用法类似rect，第一、第二、第四的参数都是相同的，只不过polygon会接受一系列坐标的列表，代表了哥哥定点。

# pygame.draw.circle
`pygame.draw.circle(Surface,color,pos,radius,width=0)`
他接受一个圆心坐标和半径参数

# pygame.draw.ellipse
`pygame.draw.ellipse(Surface,color,Rect,width=0)`
可以把一个ellipse想像成一个被压扁的圆，事实上，他是可以被一个矩形装起来的，它接受的第三个参数就是椭圆的外接矩形

# pygame.draw.arc
`pygame.draw.arc(Surface,color,Rect,start_angle,stop_angle,width=1)`
arc是椭圆的一部分，所以她的参数也就比椭圆多一点。但他是不封闭的，因此没有fill方法。start_angle和stop_angle为开始和结束的角度

# pygame.draw.line
`pygame.draw.line(surface,color,start_pos,end_pos,width=1)`

# pygame.draw.lines
`pygame.draw.lines(surface,color,closed,pointlist,width=1)`
`closed`是一个布尔变量，指明是否需要多画一条线来使这些线条闭合（感觉就和polygon一样了）。`pointlist`是一个点的数组

上面标中还有`aaline`,`aalines`，就是抗锯齿，antialiasing,效果会让画面更好看一些，模型的边就不会是锯齿形的了，这两个方法就是在画线的时候做这事情的，参数和上面一样。
