#!/usr/bin/python

import json
import os
import sys
import zlib
from datetime import datetime

import base45
import cbor2
import cv2
import qrcode
from cose.messages import CoseMessage
from PIL import Image
from pyzbar import pyzbar
from reportlab.lib import pagesizes, units
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

tempdir = "temp"


class ImmunPdf:
    def generate(self):

        if len(sys.argv) < 2:
            print("Please provide a filename.")
            exit()
        else:

            filename = sys.argv[1]

            if not os.path.isfile(filename):
                print("The provided Screenshot does not exist.")
            else:
                result = pyzbar.decode(cv2.imread(filename))

                if len(result) > 0:

                    print("raw data: \n")

                    res = result[0].data.decode("utf-8")
                    print(res)

                    b45 = res[4:]

                    decoded = base45.b45decode(b45)
                    decompressed = zlib.decompress(decoded)

                    print(decompressed)

                    # decode COSE message (no signature verification done)
                    cose = CoseMessage.decode(decompressed)
                    self.personal_data = cbor2.loads(cose.payload)
                    print(json.dumps(self.personal_data, indent=2))

                    img = qrcode.make(res)
                    img.save(os.path.join(tempdir, "code.png"))

                else:

                    print("Decoding failed.")

    def make_pdf(self):

        bigfont = 12
        smallfont = 10

        page_margin = 15
        page_height = 297
        page_width = 210

        c = canvas.Canvas("temp/immun.pdf", pagesize=pagesizes.portrait(pagesizes.A4))

        # put blue box
        box_width = 105 - page_margin
        box_height = 148 - page_margin
        box_margin = 10

        blue_width = 6

        box_p_x = page_margin
        box_w_x = box_width - page_margin
        box_b = page_height - page_margin - box_height + page_margin

        c.setFillColor(HexColor("#2054a2"))

        c.roundRect(
            box_p_x * units.mm,
            box_b * units.mm,
            box_w_x * units.mm,
            (box_height - page_margin) * units.mm,
            4,
            stroke=0,
            fill=1,
        )

        c.setFillColor(HexColor("#ffffff"))

        c.roundRect(
            (box_p_x + blue_width) * units.mm,
            (box_b + blue_width) * units.mm,
            (box_w_x - 2 * blue_width) * units.mm,
            (box_height - page_margin) * units.mm,
            4,
            stroke=0,
            fill=1,
        )

        # put QR code

        qr_size = 50

        c.drawImage(
            "temp/code.png",
            (box_p_x + box_w_x / 2 - qr_size / 2) * units.mm,
            (page_height - qr_size - page_margin - box_margin) * units.mm,
            qr_size * units.mm,
            qr_size * units.mm,
        )

        first_name = self.personal_data[-260][1]["nam"]["fn"]
        last_name = self.personal_data[-260][1]["nam"]["gn"]
        dob = self.personal_data[-260][1]["dob"]

        dobd = datetime.strptime(dob, "%Y-%m-%d")

        print(first_name)
        print(last_name)
        print(dobd)

        toppos = 220
        dist = 6
        left = box_p_x + box_margin + 6

        c.setFillColor(HexColor("#000000"))

        c.setFont("Helvetica", smallfont - 2)
        c.drawString(
            (left + 3) * units.mm, toppos * units.mm, "Scan mit CovPassCheck-App"
        )

        toppos = toppos - 4

        c.setFont("Helvetica", smallfont)
        c.drawString(left * units.mm, (toppos - dist) * units.mm, "Name:")
        c.drawString(left * units.mm, (toppos - 3 * dist) * units.mm, "Geburtsdatum:")

        c.setFont("Helvetica", bigfont)
        c.drawString(
            left * units.mm,
            (toppos - 2 * dist) * units.mm,
            last_name + " " + first_name,
        )
        c.drawString(
            left * units.mm, (toppos - 4 * dist) * units.mm, dobd.strftime("%d.%m.%Y")
        )

        c.showPage()
        c.save()


if __name__ == "__main__":

    impdf = ImmunPdf()
    impdf.generate()
    impdf.make_pdf()
