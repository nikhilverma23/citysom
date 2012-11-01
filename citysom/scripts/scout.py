import urllib2,re


def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

url ="http://www.scout.me/events--near--boston-ma?filters[radius]=25&sort[label]=relevance&sort[dir]=ASC"
req=urllib2.Request(url)
res=urllib2.urlopen(req)
main_data = res.read()
res.close()
page_data = main_data
z=main_data.find("entry first events")
main_data=main_data[z:]
a = main_data.find("main_footer")
main_data = main_data[:a]
maindata = ' '.join(main_data.split())

is_search = 1;
while(is_search != -1):

    #image
    is_search = maindata.find("<img src=\"")
    maindata = maindata[is_search+10:]
    enddata = maindata
    pro_end_pos = enddata.find("\"")
    pro_end_data = enddata[:pro_end_pos]
    print "image"
    print pro_end_data

    #next page url

    platform = enddata.find("<a href=\"")
    enddata = enddata[platform+9:]
    platformdata = enddata
    plat_end_pos = platformdata.find("\"")
    platform_end_data = platformdata[:plat_end_pos]
    print "next_page url"
    print platform_end_data
    
    if(platform_end_data != -1):
        req=urllib2.Request(platform_end_data)
        res=urllib2.urlopen(req)
        data = res.read()
        res.close()

        data_next = data.find("event-date")
        datanext = data[data_next:]
        nextdata = data
        data_end_nex = nextdata.find("<div class=\"widget reviews-widget\" id=\"reviews-widget\">")
        data_end_nex = nextdata[:data_end_nex]
        if(data_end_nex != -1):
            # timing
            event_timing = data_end_nex.find("<span class=\"value-title\"")
            if(event_timing!= -1):
                data_end_nex = data_end_nex[event_timing:]
                timingdata = data_end_nex
                timing_end_pos = timingdata.find("</span>")
                timing_end_data = timingdata[:timing_end_pos]
                timing_end_data = remove_html_tags(timing_end_data)
                print "event timing"
                print timing_end_data
    
            # phone
            
            event_phone = timingdata.find("<span class=\"facet_phone\">")
            if(event_phone!= -1):
                timingdata = timingdata[event_phone:]
                phonedata = timingdata
                phone_end_pos = phonedata.find("</span>")
                phone_end_data = phonedata[:phone_end_pos]
                phone_end_data = remove_html_tags(phone_end_data)
                print "event phone"
                print phone_end_data
            
            # place url
            
            event_place_url = timingdata.find("<div class=\"facet-url\">")
            if(event_place_url!= -1):
                timingdata = timingdata[event_place_url:]
                place_urldata = timingdata
                place_url_end_pos = place_urldata.find("</div>")
                placeurl_end_data = place_urldata[:place_url_end_pos]
                placeurl_end_data = remove_html_tags(placeurl_end_data)
                print "event placeurl"
                print placeurl_end_data
            
            # event description
            
            event_des = timingdata.find("<p class=\"facet_description\">")
            if(event_des!= -1):
                timingdata = timingdata[event_des:]
                desdata = timingdata
                des_end_pos = desdata.find("<small class=\"icon\">")
                des_end_data = desdata[:des_end_pos]
                des_end_data = remove_html_tags(des_end_data)
                print "event des"
                print des_end_data

    #title
    
    event_title = platformdata.find(">")
    platformdata = platformdata[event_title+1:]
    titledata = platformdata
    title_end_pos = titledata.find("</a>")
    title_end_data = titledata[:title_end_pos]
    print "title"
    print title_end_data

    # date
    eventdate = titledata.find("<span class=\"dtstart")
    titledata = titledata[eventdate:]
    event_date_data = titledata
    date_end_pos = event_date_data.find("</span>")
    event_end_date = event_date_data[:date_end_pos]
    events_date = remove_html_tags(event_end_date)
    print "event date"
    print events_date

    # place

    eventplace = event_date_data.find("<span class=\"specific_location\">")
    event_date_data = event_date_data[eventplace:]
    event_place_data = event_date_data
    place_end_pos = event_place_data.find("<span class=\"geo\">")
    event_end_place = event_place_data[:place_end_pos]
    events_place = remove_html_tags(event_end_place)
    print "event place"
    print events_place

    # category
    
    eventcategory = event_place_data.find("<span class=\"facet_category\">")
    if(eventcategory !=-1):
        event_place_data = event_place_data[eventcategory:]
        event_category_data = event_place_data
        category_end_pos = event_category_data.find("</span>")
        event_end_category = event_category_data[:category_end_pos]
        events_category = remove_html_tags(event_end_category)
        print "event category"
        print events_category
        
    
new_page = 0
while(new_page != 600):
    new_page = new_page+1
    n_page = str(new_page)
    page_url = "http://www.scout.me/events--near--boston-ma?page="+n_page+"&filters[radius]=25&sort[label]=relevance&sort[dir]=ASC"
    print "page_url"
    print page_url
    
    req=urllib2.Request(page_url)
    res=urllib2.urlopen(req)
    new_data = res.read()
    res.close()
    s=new_data.find("entry first events")
    new_data=new_data[s:]
    t = new_data.find("main_footer")
    new_data = new_data[:t]
    newdata = ' '.join(new_data.split())
    
    new_is_search = 1;
    while(new_is_search != -1):
    
        #image
        new_is_search = newdata.find("<img src=\"")
        newdata = newdata[new_is_search+10:]
        new_enddata = newdata
        new_pro_end_pos = new_enddata.find("\"")
        new_pro_end_data = new_enddata[:new_pro_end_pos]
        print "image"
        print new_pro_end_data
    
        #next page url
    
        new_platform = new_enddata.find("<a href=\"")
        new_enddata = new_enddata[new_platform+9:]
        new_platformdata = new_enddata
        new_plat_end_pos = new_platformdata.find("\"")
        new_platform_end_data = new_platformdata[:new_plat_end_pos]
        print "next_page url"
        print new_platform_end_data
        
        if(new_platform_end_data != -1):
            req=urllib2.Request(new_platform_end_data)
            res=urllib2.urlopen(req)
            new_data = res.read()
            res.close()
    
            new_data_next = new_data.find("event-date")
            new_datanext = new_data[new_data_next:]
            new_nextdata = new_data
            new_data_end_nex = new_nextdata.find("<div class=\"widget reviews-widget\" id=\"reviews-widget\">")
            new_data_end_nex = new_nextdata[:new_data_end_nex]
            
            # timing
            new_event_timing = new_data_end_nex.find("<span class=\"value-title\"")
            if(new_event_timing!= -1):
                new_data_end_nex = new_data_end_nex[new_event_timing:]
                new_timingdata = new_data_end_nex
                new_timing_end_pos = new_timingdata.find("</span>")
                new_timing_end_data = new_timingdata[:new_timing_end_pos]
                new_timing_end_data = remove_html_tags(new_timing_end_data)
                print "event timing"
                print new_timing_end_data
    
            # phone
            
            new_event_phone = new_timingdata.find("<span class=\"facet_phone\">")
            if(new_event_phone!= -1):
                new_timingdata = new_timingdata[new_event_phone:]
                new_phonedata = new_timingdata
                new_phone_end_pos = new_phonedata.find("</span>")
                new_phone_end_data = new_phonedata[:new_phone_end_pos]
                new_phone_end_data = remove_html_tags(new_phone_end_data)
                print "event phone"
                print new_phone_end_data
            
            # place url
            
            new_event_place_url = new_timingdata.find("<div class=\"facet-url\">")
            if(new_event_place_url!= -1):
                new_timingdata = new_timingdata[new_event_place_url:]
                new_place_urldata = new_timingdata
                new_place_url_end_pos = new_place_urldata.find("</div>")
                new_placeurl_end_data = new_place_urldata[:new_place_url_end_pos]
                new_placeurl_end_data = remove_html_tags(new_placeurl_end_data)
                print "event placeurl"
                print new_placeurl_end_data
            
            # event description
            
            new_event_des = new_timingdata.find("<p class=\"facet_description\">")
            if(new_event_des!= -1):
                new_timingdata = new_timingdata[new_event_des:]
                new_desdata = new_timingdata
                new_des_end_pos = new_desdata.find("<small class=\"icon\">")
                new_des_end_data = new_desdata[:new_des_end_pos]
                new_des_end_data = remove_html_tags(new_des_end_data)
                print "event des"
                print new_des_end_data
    
        #title
        
        new_event_title = new_platformdata.find(">")
        new_platformdata = new_platformdata[new_event_title+1:]
        new_titledata = new_platformdata
        new_title_end_pos = new_titledata.find("</a>")
        new_title_end_data = new_titledata[:new_title_end_pos]
        print "title"
        print new_title_end_data
    
        # date
        new_eventdate = new_titledata.find("<span class=\"dtstart")
        new_titledata = new_titledata[new_eventdate:]
        new_event_date_data = new_titledata
        new_date_end_pos = new_event_date_data.find("</span>")
        new_event_end_date = new_event_date_data[:new_date_end_pos]
        new_events_date = remove_html_tags(new_event_end_date)
        print "event date"
        print new_events_date
    
        # place
    
        new_eventplace = new_event_date_data.find("<span class=\"specific_location\">")
        new_event_date_data = new_event_date_data[new_eventplace:]
        new_event_place_data = new_event_date_data
        new_place_end_pos = new_event_place_data.find("<span class=\"geo\">")
        new_event_end_place = new_event_place_data[:new_place_end_pos]
        new_events_place = remove_html_tags(new_event_end_place)
        print "event place"
        print new_events_place
    
        # category
        
        new_eventcategory = new_event_place_data.find("<span class=\"facet_category\">")
        if(new_eventcategory != -1):
            new_event_place_data = new_event_place_data[new_eventcategory:]
            new_event_category_data = new_event_place_data
            new_category_end_pos = new_event_category_data.find("</span>")
            new_event_end_category = new_event_category_data[:new_category_end_pos]
            new_events_category = remove_html_tags(new_event_end_category)
            print "event category"
            print new_events_category
        
    
    
    
    
    
    

