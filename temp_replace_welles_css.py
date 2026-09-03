from pathlib import Path
path = Path(r'c:\Users\user\Documents\Шаблоны и тесты\WELLESKRILLMAIN.html')
text = path.read_text(encoding='utf-8')
start = text.index('<style type="text/css">')
end = text.index('</style>', start) + len('</style>')
new_css = '''<style type="text/css">
  html, body {
    margin:0 !important;
    padding:0 !important;
    width:100% !important;
    min-width:600px !important;
    -webkit-text-size-adjust:100% !important;
    -ms-text-size-adjust:100% !important;
  }
  body, table, td, p, a {
    margin:0;
    padding:0;
    font-family:Verdana, Tahoma, Arial, sans-serif !important;
  }
  table {
    border-collapse:collapse;
    border-spacing:0;
    mso-table-lspace:0pt;
    mso-table-rspace:0pt;
  }
  img {
    border:0;
    display:block;
    line-height:0;
    outline:none;
    text-decoration:none;
    -ms-interpolation-mode:bicubic;
  }
  body {
    background-color:#042444 !important;
    background-image:none !important;
  }
  .outer-wrapper {
    width:100% !important;
    background-color:#042444 !important;
    background-image:none !important;
  }
  .email-container {
    width:600px !important;
    min-width:600px !important;
    max-width:600px !important;
    margin:0 auto !important;
    border-radius:18px !important;
    border-collapse:separate !important;
    overflow:hidden !important;
  }
  .email-background {
    background-color:transparent !important;
    background-image:url('https://cdn.chipychapa.com/welle/Emails/content/WelleBackground.png') !important;
    background-repeat:no-repeat !important;
    background-position:top center !important;
    background-size:cover !important;
  }
  .hero-card {
    width:310px !important;
    max-width:310px !important;
    margin-left:0 !important;
    margin-right:0 !important;
    background-color:transparent !important;
  }
  .hero-top {
    font-size:24px !important;
    line-height:27px !important;
    font-weight:900 !important;
    letter-spacing:1px !important;
    text-transform:uppercase !important;
  }
  .hero-bottom {
    font-size:15px !important;
    line-height:18px !important;
    font-weight:700 !important;
    letter-spacing:1px !important;
    text-transform:uppercase !important;
  }
  .hero-logo-shift-wrap {
    width:240px !important;
    max-width:240px !important;
    margin-left:auto !important;
    margin-right:auto !important;
  }
  .hero-welle-logo {
    display:block !important;
    width:220px !important;
    max-width:220px !important;
    height:auto !important;
    margin-left:0 !important;
    margin-right:0 !important;
  }
  .left-lock-outer {
    padding-left:40px !important;
    padding-right:0 !important;
    text-align:left !important;
  }
  .compact-left-block,
  .mobile-left-lock,
  .bonus-label-table {
    width:400px !important;
    max-width:400px !important;
    margin-left:0 !important;
    margin-right:0 !important;
    background-color:transparent !important;
  }
  .bonus-label-text {
    text-align:center !important;
  }
  .wide-info-align-outer {
    padding-left:40px !important;
    padding-right:0 !important;
    text-align:left !important;
  }
  .wide-info-wrap,
  .wide-info-outer,
  .short-info-block {
    width:520px !important;
    max-width:520px !important;
    margin-left:0 !important;
    margin-right:0 !important;
  }
  .translucent-panel,
  .translucent-panel > tbody > tr > td {
    background-color:rgba(9, 38, 53, 0.50) !important;
    background-image:none !important;
  }
  .translucent-inner,
  .translucent-inner > tbody > tr > td {
    background-color:rgba(15, 49, 71, 0.50) !important;
    background-image:none !important;
  }
  .upper-matching-glass,
  .upper-matching-glass > tbody > tr > td {
    background-color:rgba(9, 38, 53, 0.50) !important;
    background-image:none !important;
    border-radius:18px !important;
    border-collapse:separate !important;
    overflow:hidden !important;
  }
  .upper-transparent-inner,
  .upper-transparent-inner > tbody > tr > td,
  .upper-transparent-inner table,
  .upper-transparent-inner table td {
    background-color:transparent !important;
    background-image:none !important;
  }
  .upper-transparent-inner td[bgcolor="#44b9f3"] {
    background-color:#44b9f3 !important;
  }
  .wide-info-outer,
  .wide-info-outer > tbody > tr > td {
    background-color:rgba(9, 38, 53, 0.50) !important;
    background-image:none !important;
  }
  @media only screen and (max-width:640px) {
    .left-lock-outer,
    .compact-left-block,
    .mobile-left-lock,
    .bonus-label-table,
    .wide-info-wrap,
    .wide-info-outer,
    .short-info-block {
      margin-left:0 !important;
      margin-right:0 !important;
    }
    .bonus-label-text {
      text-align:center !important;
    }
    .hero-welle-logo,
    .hero-logo-shift-wrap {
      margin-left:0 !important;
      margin-right:0 !important;
    }
    .translucent-panel,
    .translucent-panel > tbody > tr > td,
    .translucent-inner,
    .translucent-inner > tbody > tr > td,
    .upper-matching-glass,
    .upper-matching-glass > tbody > tr > td,
    .upper-transparent-inner,
    .upper-transparent-inner > tbody > tr > td,
    .upper-transparent-inner table,
    .upper-transparent-inner table td,
    .wide-info-outer,
    .wide-info-outer > tbody > tr > td {
      background-color:rgba(9, 38, 53, 0.50) !important;
      background-image:none !important;
    }
  }
</style>'''
path.write_text(text[:start] + new_css + text[end:], encoding='utf-8')
print('updated', path)
