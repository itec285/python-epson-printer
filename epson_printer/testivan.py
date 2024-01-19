from .epsonprinter import EpsonPrinter
from optparse import OptionParser
import sys

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-v", "--idvendor", action="store", type="int", dest="id_vendor", help="The printer vendor id")
    parser.add_option("-p", "--idProduct", action="store", type="int", dest="id_product", help="The printer product id")
    options, args = parser.parse_args()
    if not options.id_vendor or not options.id_product:
        parser.print_help()
    else:
        printer = EpsonPrinter(options.id_vendor, options.id_product)
        printer.print_text("Hello, how's it going?")
        printer.linefeed()
        printer.print_text("Part of this")
        printer.bold_on()
        printer.print_text(" line is bold")
        printer.bold_off()
        printer.linefeed()
        printer.underline_on()
        printer.print_text("Underlined")
        printer.underline_off()
        printer.linefeed()
        printer.right_justified()
        printer.print_text("Right justified")
        printer.linefeed()
        printer.center()
        printer.print_text("Center justified")
        printer.linefeed()
        printer.left_justified()
        printer.print_text("Left justified")
        printer.linefeed()
        printer.set_text_size(1, 1)
        printer.print_text("Double size text")
        printer.set_text_size(0, 0)
        printer.linefeed()
        printer.rotate_on()
        printer.print_text("Rotated Text")
        printer.rotate_off()
        printer.linefeed()
        
        #Print a QR Code in the center
        printer.center()
        printer.qr_selectmodel()
        printer.qr_setsize()
        printer.qr_errorcorrect()
        printer.qr_storedata()
        printer.qr_printdata()
        printer.linefeed()
        #Done printing QR code
        
        printer.left_justified()
        printer.print_text("Feeding paper 10 lines before cutting")
        printer.linefeed(10)
        printer.cut()
        sys.exit(1)
