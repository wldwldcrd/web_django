from django.contrib import admin
from reviews.models import (Publisher, Contributor,
                            Book, BookContributor, Review)


def initialled_name(obj):
    """ obj.first_names='Jerome David',
    obj.last_names='Salinger'=> 'Salinger, JD' """
    initials = ''.join([name[0] for name in
                        obj.first_names.split(' ')])
    return "{}, {}".format(obj.last_names, initials)


class ContributorAdmin(admin.ModelAdmin):
    list_display = (initialled_name,)


class ReviewAdmin(admin.ModelAdmin):
    # to exclude specific fields
    # exclude = ('date_edited',)

    # to select fields to display
    # fields = ('content', 'rating', 'creator', 'book',)

    # to group fields
    fieldsets = ((None, {'fields': ('creator', 'book')}),
                 ('Review content', {'fields': ('content', 'rating')}))


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13', 'has_isbn')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name')

    @admin.display(
        ordering='isbn',
        description='ISBN-13',
        empty_value='-/-'
    )
    def isbn13(self, obj):
        """ '9780316769174' => '978-0-31-676917-4' """
        return "{}-{}-{}-{}-{}".format(obj.isbn[0:3],
                                       obj.isbn[3:4],  obj.isbn[4:6],
                                       obj.isbn[6:12], obj.isbn[12:13])

    @admin.display(
        boolean=True,
        description='Has ISBN',
    )
    def has_isbn(self, obj):
        """ '9780316769174' => True """
        return bool(obj.isbn)


# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)
