from django.db.models.query import QuerySet
from django.db.models import Q 

class __PostQuerySet(QuerySet):
    """  """
    def public_posts(self):
        return self.filter(privacy = 'public')
    
    def private_posts(self, user):
        return self.filter(Q(privacy = 'private'),
                            Q(posted_by = user) | Q(recipient=user)
                            )

    def viewable_posts(self, user):
        """ all posts that can be viewd by this user both public 
            and private
        """
        combined = self.public_posts() | self.private_posts(user)
        return combined.order_by('-created')

PostManager = __PostQuerySet.as_manager
