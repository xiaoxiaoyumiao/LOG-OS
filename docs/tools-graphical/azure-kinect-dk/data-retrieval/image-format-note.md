# Image Format Note

<table>
  <thead>
    <tr>
      <th style="text-align:left">Enumerator</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">K4A_IMAGE_FORMAT_COLOR_MJPG</td>
      <td style="text-align:left">
        <p>Color image type MJPG.</p>
        <p>The buffer for each image is encoded as a JPEG and can be decoded by a
          JPEG decoder.</p>
        <p>Because the image is compressed, the stride parameter for the <a href="https://microsoft.github.io/Azure-Kinect-Sensor-SDK/master/structk4a__image__t.html">k4a_image_t</a> is
          not applicable.</p>
        <p>Each MJPG encoded image in a stream may be of differing size depending
          on the compression efficiency.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">K4A_IMAGE_FORMAT_COLOR_NV12</td>
      <td style="text-align:left">
        <p>Color image type NV12.</p>
        <p>NV12 images separate the luminance and chroma data such that all the luminance
          is at the beginning of the buffer, and the chroma lines follow immediately
          after.</p>
        <p>Stride indicates the length of each line in bytes and should be used to
          determine the start location of each line of the image in memory. Chroma
          has half as many lines of height and half the width in pixels of the luminance.
          Each chroma line has the same width in bytes as a luminance line.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">K4A_IMAGE_FORMAT_COLOR_YUY2</td>
      <td style="text-align:left">
        <p>Color image type YUY2.</p>
        <p>YUY2 stores chroma and luminance data in interleaved pixels.</p>
        <p>Stride indicates the length of each line in bytes and should be used to
          determine the start location of each line of the image in memory.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">K4A_IMAGE_FORMAT_COLOR_BGRA32</td>
      <td style="text-align:left">
        <p>Color image type BGRA32.</p>
        <p>Each pixel of BGRA32 data is four bytes. The first three bytes represent
          Blue, Green, and Red data. The fourth byte is the alpha channel and is
          unused in the Azure Kinect APIs.</p>
        <p>Stride indicates the length of each line in bytes and should be used to
          determine the start location of each line of the image in memory.</p>
        <p>The Azure Kinect device does not natively capture in this format. Requesting
          images of this format requires additional computation in the API.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">K4A_IMAGE_FORMAT_DEPTH16</td>
      <td style="text-align:left">
        <p>Depth image type DEPTH16.</p>
        <p>Each pixel of DEPTH16 data is two bytes of little endian unsigned depth
          data. The unit of the data is in millimeters from the origin of the camera.</p>
        <p>Stride indicates the length of each line in bytes and should be used to
          determine the start location of each line of the image in memory.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">K4A_IMAGE_FORMAT_IR16</td>
      <td style="text-align:left">
        <p>Image type IR16.</p>
        <p>Each pixel of IR16 data is two bytes of little endian unsigned depth data.
          The value of the data represents brightness.</p>
        <p>This format represents infrared light and is captured by the depth camera.</p>
        <p>Stride indicates the length of each line in bytes and should be used to
          determine the start location of each line of the image in memory.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">K4A_IMAGE_FORMAT_CUSTOM8</td>
      <td style="text-align:left">
        <p>Single channel image type CUSTOM8.</p>
        <p>Each pixel of CUSTOM8 is a single channel one byte of unsigned data.</p>
        <p>Stride indicates the length of each line in bytes and should be used to
          determine the start location of each line of the image in memory.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">K4A_IMAGE_FORMAT_CUSTOM16</td>
      <td style="text-align:left">
        <p>Single channel image type CUSTOM16.</p>
        <p>Each pixel of CUSTOM16 is a single channel two bytes of little endian
          unsigned data.</p>
        <p>Stride indicates the length of each line in bytes and should be used to
          determine the start location of each line of the image in memory.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">K4A_IMAGE_FORMAT_CUSTOM</td>
      <td style="text-align:left">
        <p>Custom image format.</p>
        <p>Used in conjunction with user created images or images packing non-standard
          data.</p>
        <p>See the originator of the custom formatted image for information on how
          to interpret the data.</p>
      </td>
    </tr>
  </tbody>
</table>

## Reference

[https://microsoft.github.io/Azure-Kinect-Sensor-SDK/master/group\_\_\_enumerations\_gabd9688eb20d5cb878fd22d36de882ddb.html\#ggabd9688eb20d5cb878fd22d36de882ddba5abd5fdff69181007ec79ed3087aa18e](https://microsoft.github.io/Azure-Kinect-Sensor-SDK/master/group___enumerations_gabd9688eb20d5cb878fd22d36de882ddb.html#ggabd9688eb20d5cb878fd22d36de882ddba5abd5fdff69181007ec79ed3087aa18e)

