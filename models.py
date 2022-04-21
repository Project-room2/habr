from django.db import models


class Thread(models.Model):
    id = models.ForeignKey(Habr,
                             on_delete=models.CASCADE,
                             related_name='comments')
    id_habr = models.ForeignKey(Habr, on_delete=models.SET_NULL())
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL())
    body = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    id_reply = models.ForeignKey(Reply, on_delete=models.SET_NULL()   )

    def __str__(self):
        return f"{self.body}   "


class Reply(models.Model):
    id = models.ForeignKey(Thread,
                             on_delete=models.CASCADE,
                             related_name='reply')
    body = models.TextField()
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id_replyble = models.ForeignKey(Thread, on_delete=models.SET_NULL())

    def __str__(self):
        return f"{self.body} "



