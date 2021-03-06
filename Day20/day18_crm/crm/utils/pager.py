""""
使用文档：
    pager = Pagination（当前页码数，总数据量，生成的URL）
    # 切片取数据
    all_depart = models.Department.objects.all()[pager.start:pager.end]
    # 生成li标签
    pager.page_html

    {{ page_html|safe }}

"""

class Pagination:
    def __init__(self, page, total_num,url, per_num=10, max_show=11):
        try:
            page = int(page)
            if page < 1:
                page = 1
        except Exception as e:
            page = 1
        self.url = url
        self.page = page
        self.total_num = total_num
        self.per_num = per_num
        # 总页码数
        self.total_page_num, more = divmod(self.total_num, self.per_num)
        if more:
            self.total_page_num += 1
        # 最多显示页码数
        self.max_show = max_show
        half_show = self.max_show // 2

        self.page_start = self.page - half_show  # 1
        self.page_end = self.page + half_show  # 11

        # 数据量少，不够生成11个页面的时候
        if self.total_page_num < self.max_show:
            self.page_start = 1
            self.page_end = self.total_page_num
        else:
            # 可以生成11个页码
            #  1 2 3 4 5
            if self.page <= half_show:
                self.page_start = 1
                self.page_end = self.max_show
            elif self.page + half_show > self.total_page_num:
                self.page_start = self.total_page_num - self.max_show + 1
                self.page_end = self.total_page_num
            else:
                self.page_start = self.page - half_show
                self.page_end = self.page + half_show

    @property
    def start(self):
        return (self.page - 1) * 10

    @property
    def end(self):
        return self.page * 10

    @property
    def page_html(self):
        page_list = []
        if self.page == 1:
            page_list.append('<li class="disabled"> <span aria-hidden="true">&laquo;</span>  </li>')
        else:
            page_list.append('<li><a href="{}?page={}">&laquo;</a></li>'.format(self.url,self.page - 1))

        for i in range(self.page_start, self.page_end + 1):
            if i == self.page:
                page_list.append('<li class="active"><a href="{}?page={}">{}</a></li>'.format(self.url,i, i))
            else:
                page_list.append('<li><a href="{}?page={}">{}</a></li>'.format(self.url,i, i))

        if self.page == self.total_page_num:
            page_list.append('<li class="disabled"> <span aria-hidden="true">»</span>  </li>')
        else:
            page_list.append('<li><a href="{}?page={}">»</a></li>'.format(self.url,self.page + 1))

        return ''.join(page_list)
