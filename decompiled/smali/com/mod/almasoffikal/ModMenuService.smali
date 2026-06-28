.class public Lcom/mod/almasoffikal/ModMenuService;
.super Landroid/app/Service;

.field private windowManager:Landroid/view/WindowManager;
.field private floatingView:Landroid/widget/Button;

.method public onCreate()V
    .registers 5
    invoke-super {p0}, Landroid/app/Service;->onCreate()V

    const-string v0, "window"
    invoke-virtual {p0, v0}, Lcom/mod/almasoffikal/ModMenuService;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;
    move-result-object v0
    check-cast v0, Landroid/view/WindowManager;
    iput-object v0, p0, Lcom/mod/almasoffikal/ModMenuService;->windowManager:Landroid/view/WindowManager;

    new-instance v0, Landroid/widget/Button;
    invoke-direct {v0, p0}, Landroid/widget/Button;-><init>(Landroid/content/Context;)V
    iput-object v0, p0, Lcom/mod/almasoffikal/ModMenuService;->floatingView:Landroid/widget/Button;
    iget-object v0, p0, Lcom/mod/almasoffikal/ModMenuService;->floatingView:Landroid/widget/Button;
    const-string v1, "MOD"
    invoke-virtual {v0, v1}, Landroid/widget/Button;->setText(Ljava/lang/CharSequence;)V

    new-instance v0, Landroid/view/WindowManager$LayoutParams;
    const/16 v1, -0x2
    const/16 v2, -0x2
    const/16 v3, 0x7f6
    const/16 v4, 0x8
    const/4 v5, -0x3
    invoke-direct/range {v0 .. v5}, Landroid/view/WindowManager$LayoutParams;-><init>(IIIII)V
    
    iget-object v1, p0, Lcom/mod/almasoffikal/ModMenuService;->windowManager:Landroid/view/WindowManager;
    iget-object v2, p0, Lcom/mod/almasoffikal/ModMenuService;->floatingView:Landroid/widget/Button;
    invoke-interface {v1, v2, v0}, Landroid/view/WindowManager;->addView(Landroid/view/View;Landroid/view/ViewGroup$LayoutParams;)V

    return-void
.end method

.method public onBind(Landroid/content/Intent;)Landroid/os/IBinder;
    .registers 3
    const/4 v0, 0x0
    return-object v0
.end method
