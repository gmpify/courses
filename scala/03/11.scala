import java.awt.datatransfer._
import scala.collection.mutable.Buffer
import scala.collection.JavaConversions.asScalaBuffer

val flavors = SystemFlavorMap.getDefaultFlavorMap().asInstanceOf[SystemFlavorMap]

val result : Buffer[String] = flavors.getNativesForFlavor(DataFlavor.imageFlavor)
